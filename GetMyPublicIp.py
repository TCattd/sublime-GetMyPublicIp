import sublime, sublime_plugin, urllib.request, random

class GetMyPublicIpCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for cursor in self.view.sel():
            #We could use any of this:
            ipapis = ['http://checkip.dyndns.org',
                        'http://bot.whatismyipaddress.com/',
                        'http://ipecho.net/plain',
                        'http://api.ipify.org/?format=text',
                        #'http://ifconfig.me/ip', #kind of slow
                        'http://icanhazip.com/',
                        'http://ident.me/',
                        'http://smart-ip.net/myip']
            urlgetip = random.choice(ipapis)

            response = urllib.request.urlopen(urlgetip).read().strip().decode("utf-8")

            #Cleanup for checkip @ dyndns
            response = response.replace("<html><head><title>Current IP Check</title></head><body>Current IP Address:", "").replace("</body></html>", "").strip();

            self.view.insert(edit, cursor.begin(), response)