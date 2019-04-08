import os


class BuildQED():
    GO_BIN = "/usr/bin/go"
    GO_FILE = "~/go/src/github.com/boisjacques/quic-conn/example/main.go"

    def __init__(self):
        self.compileGoFiles()

    def compileGoFiles(self):
        cmd = BuildQED.GO_BIN + " build -o qed " + BuildQED.GO_FILE
        print "Executing " + cmd
        os.system(cmd)
        os.system("mv qed /usr/bin")
