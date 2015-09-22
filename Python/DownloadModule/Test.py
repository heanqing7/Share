__author__ = 'He Anqing'
import SystemInfo.SystemConfig as System
import Download
import Exception
if __name__ == "__main__":
    system = System.SystemInfo("./System.cfg")
    savePath = system.getCsvSavePath()
    download = Download.DownloadCsv()
    print savePath
    share = Download.Share("000001","sz");
    try:
        download.download(share,savePath);
    except Exception.SavePathException,e:
        #notice : in here you need to fill a messageBox to tell user how to do
        print e.message
        print "SavePathError Please check the System.cfg"
