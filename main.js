// const electron = require('electron');
// const app = electron.app;
// const BrowserWindow = electron.BrowserWindow;
// //electron.crashReporter.start();

// var mainWindow = null;

// app.on('window-all-closed', function() {
//   //if (process.platform != 'darwin') {
//     app.quit();
//   //}
// });

// app.on('ready', function() {
//   // call python
//   var subpy = require('child_process').spawn('python', ['./webserver/app.py']);
//   var rq = require('request-promise');
//   //var mainAddr = 'http://localhost:5000/music';

//   var openWindow = function(){
//     mainWindow = new BrowserWindow({width: 680, height: 450});
//     mainWindow.setMenu(null);
//     mainWindow.setResizable(false);
//     // mainWindow.loadURL('file://' + __dirname + '/index.html');
//     mainWindow.loadURL('http://localhost:5000/music');
//     // mainWindow.webContents.openDevTools();
//     mainWindow.on('closed', function() {
//       mainWindow = null;
//       subpy.kill('SIGINT');
//       console.log('server stopped');
//     });
//   };

//   var startUp = function(){
//     rq(mainAddr)
//       .then(function(htmlString){
//         console.log('server started');
//         openWindow();
//       })
//       .catch(function(err){
//         console.log('waiting for the server start...');
//         startUp();
//       });
//   };

//   // fire!
//   startUp();
// });

const electron = require('electron')
const {app, BrowserWindow} = require('electron')
const path = require('path')
const url = require('url')
  
app.on('window-all-closed', function() {
  //if (process.platform != 'darwin') {
    app.quit();
  //}
});

function createWindow () {
  var subpy = require('child_process').spawn('python', ['./webserver/app.py']);
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 680, height: 450, 
    resizable: false,
    fullscreen: false
  });
  mainWindow.setMenu(null);
  //mainWindow.setResizable(false);
  // and load the index.html of the app.
  mainWindow.loadURL(url.format({
    pathname: path.join(__dirname, 'public/index.html'),
    protocol: 'file:',
    slashes: true
  }));
  mainWindow.on('closed', function() {
    mainWindow = null;
    subpy.kill('SIGINT');
    console.log('server stopped');
  });
}

app.on('ready', createWindow);