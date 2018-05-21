function openRandomMusicPlayer() { // 랜덤 음악을 재생하는 플레이어 윈도우 열기
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
    musicWindow.loadURL('http://localhost:5000/music-random');
    musicWindow.webContents.session.clearCache(function(){});
}
function openMusicPlayer(filename) { // 특정 음악을 재생하는 플레이어 윈도우 열기
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
    musicWindow.loadURL('http://localhost:5000/play/' + filename);
    // musicWindow.webContents.openDevTools();    
    musicWindow.webContents.session.clearCache(function(){});
}