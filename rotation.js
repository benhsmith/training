function randomNumber(min, max) {
  var diff = max - min;
  return max - Math.round(Math.random() * diff);
}

function pickFromArray(arr) {
    return arr[randomNumber(0, arr.length - 1)];
}

var qImage = document.getElementById("QuestionImage");
var tImage = document.getElementById("TestImage");
var Feedback = document.getElementById("Feedback");

var files = ["R.png", "Z.png", "F.png", "Q.png", "S.png", "P.png", "G.png"];
var angles = [0, 90, 45, 60, 120, 180];
var same = false;
var transform = "";

function pickLetter() {
    var index = randomNumber(0, files.length - 1);
    qImage.src = files[index];
}

function pickTest() {
    //Are we showing the same image or not?
    same = randomNumber(0, 1);
    tImage.src = qImage.src;
    var rotate = pickFromArray(angles);
    transform = "transform: rotate(" + rotate + "deg)";

    if(!same)
    {
        transform += "scaleX(-1)";
    }

    tImage.setAttribute("style", transform);
}

function newRound() {
    Feedback.textContent = "";

    pickLetter();
    pickTest();
}

function Same(response) {
    if (response == same)
    {
        //Feedback.textContent = "Yes!";
        newRound();
    }
    else
    {
        Feedback.textContent = "NO";
        Feedback.textContent += " - " + transform;
    }
}

newRound();
