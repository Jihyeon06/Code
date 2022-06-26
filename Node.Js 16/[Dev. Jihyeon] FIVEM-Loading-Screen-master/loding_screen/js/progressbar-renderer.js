Init();

//Cache to keep track of all progress values.
//This is need for the Math.max functions (so no backwards progressbars).
var progressCache = [];

function Init()
{
    //TODO: This does not belong in here...
    var logo = document.getElementById("logo");

    if(config.enableImage)
    {
        logo.setAttribute("src", config.image);
        logo.setAttribute("width", config.imageSize[0]);
        logo.setAttribute("height", config.imageSize[1]);
    }
    else
    {
        logo.setAttribute("src", config.image);
        logo.setAttribute("width", config.imageSize[0]);
        logo.style.visibility = "hidden";
    }

    var cursor = document.getElementById("cursor");
    cursor.setAttribute("src", config.cursorImage);

    //Start with random message.
    var message = document.getElementById("message");
    var index = lib.rand(0, config.loadingMessages.length);
    message.innerHTML = config.loadingMessages[index];

    //Account for transition time (about ~400ms).
    setInterval(RotateMessage, (config.loadingMessageSpeed + 400));
}

// Rotate message, load new message every x milliseconds.
function RotateMessage()
{
    lib.fadeInOut(600, "message", 0, 1);

    setTimeout(function()
    {
        var message = document.getElementById("message");
        var index = lib.rand(0, config.loadingMessages.length);      
        message.innerHTML = config.loadingMessages[index];
    }, 600);
}

