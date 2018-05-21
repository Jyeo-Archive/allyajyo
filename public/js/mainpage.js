function openPlaylist() {
    const remote = require('electron').remote;
    const BrowserWindow = remote.BrowserWindow;
    var musicWindow = new BrowserWindow({
      width: 500, height: 500,
      resizable: false,
      fullscreen: false,
      frame: false
    });
    musicWindow.setMenu(null);
    //musicWindow.setResizable(false);
    musicWindow.loadURL('http://localhost:5000/playlist');
    // musicWindow.webContents.openDevTools();
    musicWindow.webContents.session.clearCache(function(){});
}
function openFileAnalyzer() {
    const remote = require('electron').remote;
    const BrowserWindow = remote.BrowserWindow;
    var fileWindow = new BrowserWindow({
      width: 1000, height: 700
    });
    fileWindow.setMenu(null);
    //fileWindow.setResizable(false);
    fileWindow.loadURL('http://localhost:5000/file-analysis');
    fileWindow.webContents.session.clearCache(function(){});    
}