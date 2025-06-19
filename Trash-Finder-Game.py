from flask import Flask, render_template_string,request
import threading
import webbrowser
import random

app = Flask(__name__)
GOOGLE_MAPS_API_KEY = "AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE"
# HTML templates
home_P= """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trash Finding Game</title>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
        body {
            background-image: url("{{ url_for('static', filename='classic.jpg') }}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
        
            color: white;
            font-family: 'Press Start 2P', cursive;
            text-align: center;
            margin: 0;
            height: 100vh;
            position: relative;
        }

        h1 {
            margin-top: 20px;
            }
            
        .footer {
            position: absolute;
            bottom: 10px;
            left: 10px;
            color: orange	;
            font-size: 15px;
        }
        
        .button-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}

    </style>
</head>
<body>

    <h1>TRASH FINDING GAME</h1>
 <div class="button-container">
 
 <form action="/next" method="GET">
        <button type="submit" class="center-button">START</button>
    </form>

</div>
<div class="footer">Made by Anshul Laxane</div>

</body>
</html>

"""

next_P= """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <title>TRASH FINDING GAME</title>
    <style>
body{
            background-image: url("{{ url_for('static', filename='rider.jpg') }}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color: white;
            font-family: 'Press Start 2P', cursive;
            text-align: center;
            margin: 0;
            height: 100vh;
            position: relative;

}
   h1 {
            margin-top: 20px;
            }

             h4 {
            font-family: "Press Start 2P", cursive;
            color: white;
            font-weight: bold;
            text-shadow: 1px 1px 0px black;
            font-size: 30px; /* Fixed font-size */
            text-align: center;
            margin-bottom: 5px; /* Adjust spacing */
             position: absolute;
            top: 30%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .footer {
            position: absolute;
            bottom: 10px;
            left: 10px;
            color: orange	;
            font-size: 15px;
        }

        input {
            width: 250px;
            padding: 10px;
            border: 2px solid #ff5733;
            border-radius: 10px;
            background-color: #f0f8ff;
            color: #333;
            font-size: 20px;
            font-weight: bold;
            font-family: "Arial", cursive; /* Fixed font-family */
            text-align: center;
            display: block;
            margin: 20px auto; /* Centers input */
            outline: none;
            transition: all 0.3s ease-in-out;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        input:hover {
            border-color: #ffcc00;
        }

        input:focus {
            border-color: #008cff;
            background-color: #e6f7ff;
            box-shadow: 0px 0px 10px #ff4500;
        }

        input::placeholder {
            color: gray;
            font-style: italic;
            opacity: 0.7;
        }

        .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-container {
            position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}

    </style>
</head>
<body>
  <h1>Welcome to the Trash Finding Game</h1>
    <div class="container">
      <h4>ENTER YOUR USERNAME</h4>
  <form action="/game" method="GET">  <!-- Form wraps both elements -->
      <input type="text" name="username" id="playerNameInput" placeholder="Enter Your Username" required> 
        <div class="button-container">
                <button type="submit" class="center-button">PLAY</button>
        </div>
    </div>



      <div class="footer">Made by Anshul Laxane</div>
</body>
</html>

"""
content_P="""
<!DOCTYPE html>

<html lang="en">

<head> 

<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">

<title>TRASH FINDING GAME</title>
<style>
body{
            background-image: url("{{ url_for('static', filename='aurora.jpg') }}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color: white;
            font-family: 'Press Start 2P', cursive;
            text-align: center;
            margin: 0;
            height: 100vh;
            position: relative;

}

 h1 {
            text-align: center;
            margin-top: 20px;
            font-family: "Press Start 2P", cursive;
            font-weight: bold;
            text-shadow: 1px 1px 0px black;
            font-size: 30px; /* Fixed font-size */
            
            }

h3{

            text-align: center;

 position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);



}


p{
            text-align: center;

 position: absolute;
            top: 20%;
            left: 50%;
            transform: translate(-50%, -50%);


}

            
 .footer {
            position: absolute;
            bottom: 10px;
            left: 10px;
            color: orange	;
            font-size: 15px;
        }
           table {
            width: 80%;  /* Adjust width */
            margin: 20px auto; /* Center table with margin */
            border-collapse: collapse; /* Remove double borders */
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        
        th, td {
            border: 2px solid black; /* Border for each cell */
            padding: 12px; /* Add space inside cells */
            text-align: center; /* Center align text */
        }
        
        th {
            background-color: black; /* Header background color */
            color: yellow; /* Header text color */
            font-size: 20px;
        }
        
        td {
            font-size: 20px;
        }
               
        tr:hover {
            background-color: black; /* Highlight row on hover */
        }

        .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-container {
            position: absolute;
            top: 85%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}



</style>

</head> 

<body>     

<h1>TRASH FINDING GAME</h1>   

    <table>
        <tr>
            <th>Region</th>
            <th>Cities</th>
        </tr>
        <tr>
            <td>North India</td>
            <td>Delhi,Chandigarh </td>
        </tr>
        <tr>
            <td>South India</td>
            <td>Bangalore, Chennai</td>
        </tr>
        <tr>
            <td>West India</td>
            <td>Mumbai, Pune</td>
        </tr>
        <tr>
            <td>East India</td>
            <td>Kolkata,Patna</td>
        </tr>
    </table>
  <div class="button-container">
     <form action="/play1"> 
        <button type="submit" class ="center-button">PLAY GAME</button>
     </form>
</div>
     <div class="footer">Made by Anshul Laxane</div>


 <h3>Welcome, {{ username }}!</h3> 
    <p>The game begins now...</p>    
</body>

</html>
"""
play_P1="""
 <!DOCTYPE html>
<html>
<head>
    <title>GAME Page</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
     #street-view {
            width: 70%;
            height: 70vh; /* Full screen */
            border: none;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);     
        }
        #message { 
        
        color: white; font-weight: bold; 
        position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);   
        }
        
    body{
            background-image: url("{{ url_for('static', filename='retro.jpg') }}");
    
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color:black;
            font-family: 'Press Start 2P', cursive;
            margin: 0;
            height: 100vh;
            position: relative;

}
h1{


text-align: center;

}


h4{
color:black;
font-size:30
text-align:center;
font-weight: bold;
position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h5{
position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);

color:#00ff00;
text-align:center;
font-size:15;
font-weight: bold;


}

h7{

color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 102.5%;
            left: 35%;
            transform: translate(-50%, -50%);
}
p{
color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 100%;
            left: 65%;
            transform: translate(-50%, -50%);
}
h8{
color:white;
font-weight:bold;
position: absolute;
            top: 101.5%;
            left: 50%;
            transform: translate(-50%, -50%);


}



h9{
color:orange;
font-size:10;
position: absolute;
            top: 102.5%;
            left: 10%;
            transform: translate(-50%, -50%);



}
  .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-containeR {
            position: absolute;
            top: 85%;
            left: 30%;
            transform: translate(-50%, -50%);                           
        }
        .button-container {
            
            position: absolute;
            top: 85%;
            left: 70%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 10px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .Center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        .Center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
.Center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
 .Button-containeR {
            position: absolute;
            top: 95%;
            left: 35%;
            transform: translate(-50%, -50%);                           
        }

 .bUtton-containeR {
            position: absolute;
            top: 95%;
            left: 40%;
            transform: translate(-50%, -50%);                           
        }


 .buTton-containeR {
            position: absolute;
            top: 95%;
            left: 50%;
            transform: translate(-50%, -50%);                           
        }


 .buttOn-containeR {
            position: absolute;
            top: 95%;
            left: 60%;
            transform: translate(-50%, -50%);                           
        }
        .BUTTON-container{
position: absolute;
            top: 50%;
            left: 92%;
            transform: translate(-50%, -50%);   
            
        }



 .buttoN-containeR {
            position: absolute;
            top: 95%;
            left: 65%;
            transform: translate(-50%, -50%);                           
        }
        
    </style>
</head>
<body>

<script>
    function changeColor(btn) {
        btn.style.background = "orange"; // Change to orange when clicked
        btn.style.color = "white"; // Optional: Change text color for better visibility
    }
</script>


<div id="street-view"></div>
 <h3 id="message"></h3>
    <script>
    let panorama;
       function loadRandomStreetview() {
    // Define India's latitude & longitude range
    // Generate a random lat/lng
    const lngMin = 73.7800, lngMax = 73.9200; //  PUNE City 
    const latMin = 18.4800, latMax =18.5204;   // 

    const randomLat = latMin + Math.random() * (latMax - latMin);
    const randomLng = lngMin + Math.random() * (lngMax - lngMin);

    const messageContainer = document.getElementById("message");
    const streetViewService = new google.maps.StreetViewService();
    const streetViewContainer = document.getElementById("street-view");
    const randomLocation = { lat: randomLat, lng: randomLng };
    streetViewService.getPanorama({ location: randomLocation, radius: 50 }, (data, status) => {
               
        if (status === "OK" && data.location.pano) {
            messageContainer.innerHTML = "";
        panorama = new google.maps.StreetViewPanorama(streetViewContainer, {
              pano: data.location.pano,
              pov: { heading: 270, pitch: 0 },
             zoom: 1
        });


    } else {
                    console.log("No movable Street View found, trying again...");
                    messageContainer.innerHTML = "No movable Street View found, trying again...";
                    loadRandomStreetView(); // Retry if the location isn't navigable
                }
            });
        }

    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE&callback=loadRandomStreetview" async defer></script>

 
    <h1>Find Trash In Indian Cities.</h1>

    <h5>City: PUNE</h5>
    <h4>TRASH </h4>
    
   <div class="button-containeR">
 <button type="submit" class="center-button"  class="retro-button"  onclick="changeColor(this)">YES</button> 
 </div>

   <div class="button-container">
 
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">NO</button>
    </div>

  <div class="Button-containeR">
    <form action="/play2"> 
     <button type="submit" class="Center-button">1</button>
   </form>
    </div>
   
  <div class="bUtton-containeR">
  <form action="/play2"> 
 <button type="submit" class="Center-button">2</button>
   </form>
    </div>

  <div class="buTton-containeR">
  <form action="/play2"> 
 <button type="submit" class="Center-button">3</button>
   </form>
    </div>


  <div class="buttOn-containeR">
  <form action="/play2"> 
 <button type="submit" class="Center-button">4</button>
   </form>
    </div>



  <div class="buttoN-containeR">
  <form action="/play2"> 
 <button type="submit" class="Center-button">5</button>
   </form>
    </div>


<h7> BADDDD </h7>
<h8> NEUTRAL</h8>
<p> G000DD </p>
     <h9>By-Anshul Laxane</h9>


    
<div class="BUTTON-container">
 <button onclick="location.reload()" class="center-button">Get Random Street View</button>

 </div>
 
</body>
</html>
"""
play_P2="""
 <!DOCTYPE html>
<html>
<head>
    <title>GAME Page</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
     #street-view {
            width: 70%;
            height: 70vh; /* Full screen */
            border: none;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);     
        }
        #message { 
        
        color: white; font-weight: bold; 
        position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);   
        }
        
    body{
            background-image: url("{{ url_for('static', filename='retro.jpg') }}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color:black;
            font-family: 'Press Start 2P', cursive;
            margin: 0;
            height: 100vh;
            position: relative;

}
h1{


text-align: center;

}
h3{
color:Lime;
text-align: center;
font-size:15px;
position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h4{
color:black;
font-size:30
text-align:center;
font-weight: bold;
position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
}


h7{

color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 102.5%;
            left: 35%;
            transform: translate(-50%, -50%);
}
p{
color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 100%;
            left: 65%;
            transform: translate(-50%, -50%);
}
h8{
color:white;
font-weight:bold;
position: absolute;
            top: 101.5%;
            left: 50%;
            transform: translate(-50%, -50%);

}
h9{
color:orange;
font-size:10;
position: absolute;
            top: 102.5%;
            left: 10%;
            transform: translate(-50%, -50%);



}
  .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-containeR {
            position: absolute;
            top: 85%;
            left: 30%;
            transform: translate(-50%, -50%);                           
        }
        .button-container {
            
            position: absolute;
            top: 85%;
            left: 70%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 10px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .Center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        .Center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
.Center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
 .Button-containeR {
            position: absolute;
            top: 95%;
            left: 35%;
            transform: translate(-50%, -50%);                           
        }

 .bUtton-containeR {
            position: absolute;
            top: 95%;
            left: 40%;
            transform: translate(-50%, -50%);                           
        }


 .buTton-containeR {
            position: absolute;
            top: 95%;
            left: 50%;
            transform: translate(-50%, -50%);                           
        }


 .buttOn-containeR {
            position: absolute;
            top: 95%;
            left: 60%;
            transform: translate(-50%, -50%);                           
        }
        .BUTTON-container{
position: absolute;
            top: 50%;
            left: 92%;
            transform: translate(-50%, -50%);   
            
        }



 .buttoN-containeR {
            position: absolute;
            top: 95%;
            left: 65%;
            transform: translate(-50%, -50%);                           
        }
        
    </style>
</head>
<body>

<script>
    function changeColor(btn) {
        btn.style.background = "orange"; // Change to orange when clicked
        btn.style.color = "white"; // Optional: Change text color for better visibility
    }
</script>



<div id="street-view"></div>

 <h3 id="message"></h3>
    <script>
    let panorama;
       function loadRandomStreetview() {
    // Define India's latitude & longitude range
    // Generate a random lat/lng
    const lngMin = 72.78, lngMax = 72.88; //  MUMBAI City 
    const latMin = 18.90, latMax =19.20;   // 

    const randomLat = latMin + Math.random() * (latMax - latMin);
    const randomLng = lngMin + Math.random() * (lngMax - lngMin);

    const messageContainer = document.getElementById("message");
    const streetViewService = new google.maps.StreetViewService();
    const streetViewContainer = document.getElementById("street-view");
    const randomLocation = { lat: randomLat, lng: randomLng };
    streetViewService.getPanorama({ location: randomLocation, radius: 50 }, (data, status) => {
               
        if (status === "OK" && data.location.pano) {
            messageContainer.innerHTML = "";
        panorama = new google.maps.StreetViewPanorama(streetViewContainer, {
              pano: data.location.pano,
              pov: { heading: 270, pitch: 0 },
             zoom: 1
        });


    } else {
                    console.log("No movable Street View found, trying again...");
                    messageContainer.innerHTML = "No movable Street View found, trying again...";
                    loadRandomStreetView(); // Retry if the location isn't navigable
                }
            });
        }

    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE&callback=loadRandomStreetview" async defer></script>

 
    <h1>Find Trash In Indian Cities.</h1>

    <h3>City: MUMBAI</h3>
    <h4>TRASH </h4>
    
   <div class="button-containeR">
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">YES</button> 
 </div>
 
   <div class="button-container">
 
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">NO</button>
    </div>


  <div class="Button-containeR">
<form action="/play3"> 
 <button type="submit" class="Center-button">1</button>
    </div>
</form>

  <div class="bUtton-containeR">
 <form action="/play3"> 
 <button type="submit" class="Center-button">2</button>
    </div>
</form>


  <div class="buTton-containeR">
 <form action="/play3">  
 <button type="submit" class="Center-button">3</button>
    </div>
</form>

  <div class="buttOn-containeR">
  <form action="/play3"> 
 <button type="submit" class="Center-button">4</button>
    </div>
</form>


  <div class="buttoN-containeR">
  <form action="/play3"> 
 <button type="submit" class="Center-button">5</button>
    </div>
</form>

<h7> BADDDD </h7>
<h8> NEUTRAL</h8>
<p> G000DD </p>
     <h9>By-Anshul Laxane</h9>


    
<div class="BUTTON-container">
 <button onclick="location.reload()" class="center-button">Get Random Street View</button>

 </div>
 
</body>
</html>
"""
play_P3="""
 <!DOCTYPE html>
<html>
<head>
    <title>GAME Page</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
     #street-view {
            width: 70%;
            height: 70vh; /* Full screen */
            border: none;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);     
        }
        #message { 
        
        color: white; font-weight: bold; 
        position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);   
        }
        
    body{
    
            background-image: url("{{ url_for('static', filename='retro.jpg') }}");
    
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color:black;
            font-family: 'Press Start 2P', cursive;
            margin: 0;
            height: 100vh;
            position: relative;

}
h1{


text-align: center;

}
h3{
color:Lime;
text-align: center;
font-size:15px;
position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h4{
color:black;
font-size:30
text-align:center;
font-weight: bold;
position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
}



h7{

color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 102.5%;
            left: 35%;
            transform: translate(-50%, -50%);
}
p{
color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 100%;
            left: 65%;
            transform: translate(-50%, -50%);
}
h8{
color:white;
font-weight:bold;
position: absolute;
            top: 101.5%;
            left: 50%;
            transform: translate(-50%, -50%);

}
h9{
color:orange;
font-size:10;
position: absolute;
            top: 102.5%;
            left: 10%;
            transform: translate(-50%, -50%);



}
  .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-containeR {
            position: absolute;
            top: 85%;
            left: 30%;
            transform: translate(-50%, -50%);                           
        }
        .button-container {
            
            position: absolute;
            top: 85%;
            left: 70%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 10px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .Center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        .Center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
.Center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
 .Button-containeR {
            position: absolute;
            top: 95%;
            left: 35%;
            transform: translate(-50%, -50%);                           
        }

 .bUtton-containeR {
            position: absolute;
            top: 95%;
            left: 40%;
            transform: translate(-50%, -50%);                           
        }


 .buTton-containeR {
            position: absolute;
            top: 95%;
            left: 50%;
            transform: translate(-50%, -50%);                           
        }


 .buttOn-containeR {
            position: absolute;
            top: 95%;
            left: 60%;
            transform: translate(-50%, -50%);                           
        }
        .BUTTON-container{
position: absolute;
            top: 50%;
            left: 92%;
            transform: translate(-50%, -50%);   
            
        }



 .buttoN-containeR {
            position: absolute;
            top: 95%;
            left: 65%;
            transform: translate(-50%, -50%);                           
        }
        
    </style>
</head>
<body>

<script>
    function changeColor(btn) {
        btn.style.background = "orange"; // Change to orange when clicked
        btn.style.color = "white"; // Optional: Change text color for better visibility
    }
</script>



<div id="street-view"></div>
 <h3 id="message"></h3>
    <script>
    let panorama;
       function loadRandomStreetview() {
    // Define India's latitude & longitude range
    // Generate a random lat/lng
    const lngMin = 88.25, lngMax = 88.50; //  GUWHATI City 
    const latMin = 22.45, latMax =22.75;   // 

    const randomLat = latMin + Math.random() * (latMax - latMin);
    const randomLng = lngMin + Math.random() * (lngMax - lngMin);

    const messageContainer = document.getElementById("message");
    const streetViewService = new google.maps.StreetViewService();
    const streetViewContainer = document.getElementById("street-view");
    const randomLocation = { lat: randomLat, lng: randomLng };
    streetViewService.getPanorama({ location: randomLocation, radius: 50 }, (data, status) => {
               
        if (status === "OK" && data.location.pano) {
            messageContainer.innerHTML = "";
        panorama = new google.maps.StreetViewPanorama(streetViewContainer, {
              pano: data.location.pano,
              pov: { heading: 270, pitch: 0 },
             zoom: 1
        });


    } else {
                    console.log("No movable Street View found, trying again...");
                    messageContainer.innerHTML = "No movable Street View found, trying again...";
                    loadRandomStreetView(); // Retry if the location isn't navigable
                }
            });
        }

    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE&callback=loadRandomStreetview" async defer></script>

 
    <h1>Find Trash In Indian Cities.</h1>

    <h3>City: Kolkata</h3>
    <h4>TRASH </h4>

    
   <div class="button-containeR">
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">YES</button> 
 </div>
 
   <div class="button-container">
 
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">NO</button>
    </div>


  <div class="Button-containeR">
 <form action="/play4"> 
 <button type="submit" class="Center-button">1</button>
 </form>
    </div>

  <div class="bUtton-containeR">
 <form action="/play4"> 
 <button type="submit" class="Center-button">2</button>
 </form>
 
    </div>

  <div class="buTton-containeR">
 <form action="/play4"> 
 <button type="submit" class="Center-button">3</button>
 </form>
 
    </div>


  <div class="buttOn-containeR">
 <form action="/play4"> 
 <button type="submit" class="Center-button">4</button>
 </form>
 
    </div>



  <div class="buttoN-containeR">
 <form action="/play4"> 
 <button type="submit" class="Center-button">5</button>
 </form>

    </div>


<h7> BADDDD </h7>
<h8> NEUTRAL</h8>
<p> G000DD </p>
     <h9>By-Anshul Laxane</h9>


    
<div class="BUTTON-container">
 <button onclick="location.reload()" class="center-button">Get Random Street View</button>

 </div>
 
</body>
</html>

"""
play_P4="""
 <!DOCTYPE html>
<html>
<head>
    <title>GAME Page</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
     #street-view {
            width: 70%;
            height: 70vh; /* Full screen */
            border: none;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);     
        }
        #message { 
        
        color: white; font-weight: bold; 
        position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);   
        }
        
    body{
    
            background-image: url("{{ url_for('static', filename='retro.jpg') }}");
        
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color:black;
            font-family: 'Press Start 2P', cursive;
            margin: 0;
            height: 100vh;
            position: relative;

}
h1{


text-align: center;

}
h3{
color:Lime;
text-align: center;
font-size:15px;
position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h4{
color:black;
font-size:30
text-align:center;
font-weight: bold;
position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
}


h7{

color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 102.5%;
            left: 35%;
            transform: translate(-50%, -50%);
}
p{
color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 100%;
            left: 65%;
            transform: translate(-50%, -50%);
}
h8{
color:white;
font-weight:bold;
position: absolute;
            top: 101.5%;
            left: 50%;
            transform: translate(-50%, -50%);

}
h9{
color:orange;
font-size:10;
position: absolute;
            top: 102.5%;
            left: 10%;
            transform: translate(-50%, -50%);



}
  .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-containeR {
            position: absolute;
            top: 85%;
            left: 30%;
            transform: translate(-50%, -50%);                           
        }
        .button-container {
            
            position: absolute;
            top: 85%;
            left: 70%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 10px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .Center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        .Center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
.Center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
 .Button-containeR {
            position: absolute;
            top: 95%;
            left: 35%;
            transform: translate(-50%, -50%);                           
        }

 .bUtton-containeR {
            position: absolute;
            top: 95%;
            left: 40%;
            transform: translate(-50%, -50%);                           
        }


 .buTton-containeR {
            position: absolute;
            top: 95%;
            left: 50%;
            transform: translate(-50%, -50%);                           
        }


 .buttOn-containeR {
            position: absolute;
            top: 95%;
            left: 60%;
            transform: translate(-50%, -50%);                           
        }
        .BUTTON-container{
position: absolute;
            top: 50%;
            left: 92%;
            transform: translate(-50%, -50%);   
            
        }



 .buttoN-containeR {
            position: absolute;
            top: 95%;
            left: 65%;
            transform: translate(-50%, -50%);                           
        }
        
    </style>
</head>
<body>

<script>
    function changeColor(btn) {
        btn.style.background = "orange"; // Change to orange when clicked
        btn.style.color = "white"; // Optional: Change text color for better visibility
    }
</script>




<div id="street-view"></div>
 <h3 id="message"></h3>
    <script>
    let panorama;
       function loadRandomStreetview() {
    // Define India's latitude & longitude range
    // Generate a random lat/lng
    const lngMin = 76.69, lngMax = 76.84; //  chandigarh City 
    const latMin = 30.66, latMax =30.80;   // 

    const randomLat = latMin + Math.random() * (latMax - latMin);
    const randomLng = lngMin + Math.random() * (lngMax - lngMin);

    const messageContainer = document.getElementById("message");
    const streetViewService = new google.maps.StreetViewService();
    const streetViewContainer = document.getElementById("street-view");
    const randomLocation = { lat: randomLat, lng: randomLng };
    streetViewService.getPanorama({ location: randomLocation, radius: 50 }, (data, status) => {
               
        if (status === "OK" && data.location.pano) {
            messageContainer.innerHTML = "";
        panorama = new google.maps.StreetViewPanorama(streetViewContainer, {
              pano: data.location.pano,
              pov: { heading: 270, pitch: 0 },
             zoom: 1
        });


    } else {
                    console.log("No movable Street View found, trying again...");
                    messageContainer.innerHTML = "No movable Street View found, trying again...";
                    loadRandomStreetView(); // Retry if the location isn't navigable
                }
            });
        }

    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE&callback=loadRandomStreetview" async defer></script>

 
    <h1>Find Trash In Indian Cities.</h1>

    <h3>City: Chandigarh</h3>
    <h4>TRASH </h4>
    
   <div class="button-containeR">
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">YES</button> 
 </div>
 
   <div class="button-container">
 
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">NO</button>
    </div>


  <div class="Button-containeR">
 <form action="/play5"> 
 <button type="submit" class="Center-button">1</button>
 </form>
    </div>

  <div class="bUtton-containeR">
 <form action="/play5"> 
 <button type="submit" class="Center-button">2</button>
 </form>
 
    </div>

  <div class="buTton-containeR">
 <form action="/play5"> 
 <button type="submit" class="Center-button">3</button>
 </form>
 
    </div>


  <div class="buttOn-containeR">
 <form action="/play5"> 
 <button type="submit" class="Center-button">4</button>
 </form>
 
    </div>



  <div class="buttoN-containeR">
 <form action="/play5"> 
 <button type="submit" class="Center-button">5</button>
 </form>

    </div>


<h7> BADDDD </h7>
<h8> NEUTRAL</h8>
<p> G000DD </p>
     <h9>By-Anshul Laxane</h9>


    
<div class="BUTTON-container">
 <button onclick="location.reload()" class="center-button">Get Random Street View</button>

 </div>
 
</body>
</html>

"""
play_P5="""
 <!DOCTYPE html>
<html>
<head>
    <title>GAME Page</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
     #street-view {
            width: 70%;
            height: 70vh; /* Full screen */
            border: none;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);     
        }
        #message { 
        
        color: white; font-weight: bold; 
        position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);   
        }
        
    body{
    
            background-image: url("{{ url_for('static', filename='retro.jpg') }}");
     
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color:black;
            font-family: 'Press Start 2P', cursive;
            margin: 0;
            height: 100vh;
            position: relative;

}
h1{


text-align: center;

}
h3{
color:Lime;
text-align: center;
font-size:15px;
position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h4{
color:black;
font-size:30
text-align:center;
font-weight: bold;
position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
}




h7{

color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 102.5%;
            left: 35%;
            transform: translate(-50%, -50%);
}
p{
color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 100%;
            left: 65%;
            transform: translate(-50%, -50%);
}
h8{
color:white;
font-weight:bold;
position: absolute;
            top: 101.5%;
            left: 50%;
            transform: translate(-50%, -50%);

}
h9{
color:orange;
font-size:10;
position: absolute;
            top: 102.5%;
            left: 10%;
            transform: translate(-50%, -50%);



}
  .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-containeR {
            position: absolute;
            top: 85%;
            left: 30%;
            transform: translate(-50%, -50%);                           
        }
        .button-container {
            
            position: absolute;
            top: 85%;
            left: 70%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 10px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .Center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        .Center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
.Center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
 .Button-containeR {
            position: absolute;
            top: 95%;
            left: 35%;
            transform: translate(-50%, -50%);                           
        }

 .bUtton-containeR {
            position: absolute;
            top: 95%;
            left: 40%;
            transform: translate(-50%, -50%);                           
        }


 .buTton-containeR {
            position: absolute;
            top: 95%;
            left: 50%;
            transform: translate(-50%, -50%);                           
        }


 .buttOn-containeR {
            position: absolute;
            top: 95%;
            left: 60%;
            transform: translate(-50%, -50%);                           
        }
        .BUTTON-container{
position: absolute;
            top: 50%;
            left: 92%;
            transform: translate(-50%, -50%);   
            
        }



 .buttoN-containeR {
            position: absolute;
            top: 95%;
            left: 65%;
            transform: translate(-50%, -50%);                           
        }
        
    </style>
</head>
<body>

<script>
    function changeColor(btn) {
        btn.style.background = "orange"; // Change to orange when clicked
        btn.style.color = "white"; // Optional: Change text color for better visibility
    }
</script>


<div id="street-view"></div>
 <h3 id="message"></h3>
    <script>
    let panorama;
       function loadRandomStreetview() {
    // Define India's latitude & longitude range
    // Generate a random lat/lng
    const lngMin =76.83, lngMax = 77.23; //  DELHI City 
    const latMin = 28.47, latMax =28.90;   // 

    const randomLat = latMin + Math.random() * (latMax - latMin);
    const randomLng = lngMin + Math.random() * (lngMax - lngMin);

    const messageContainer = document.getElementById("message");
    const streetViewService = new google.maps.StreetViewService();
    const streetViewContainer = document.getElementById("street-view");
    const randomLocation = { lat: randomLat, lng: randomLng };
    streetViewService.getPanorama({ location: randomLocation, radius: 50 }, (data, status) => {
               
        if (status === "OK" && data.location.pano) {
            messageContainer.innerHTML = "";
        panorama = new google.maps.StreetViewPanorama(streetViewContainer, {
              pano: data.location.pano,
              pov: { heading: 270, pitch: 0 },
             zoom: 1
        });


    } else {
                    console.log("No movable Street View found, trying again...");
                    messageContainer.innerHTML = "No movable Street View found, trying again...";
                    loadRandomStreetView(); // Retry if the location isn't navigable
                }
            });
        }

    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE&callback=loadRandomStreetview" async defer></script>

 
    <h1>Find Trash In Indian Cities.</h1>

    <h3>City: Delhi</h3>
    <h4>TRASH </h4>
    
   <div class="button-containeR">
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">YES</button> 
 </div>
 
   <div class="button-container">
 
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">NO</button>
    </div>


  <div class="Button-containeR">
 <form action="/play6"> 
 <button type="submit" class="Center-button">1</button>
 </form>
    </div>

  <div class="bUtton-containeR">
 <form action="/play6"> 
 <button type="submit" class="Center-button">2</button>
 </form>
 
    </div>

  <div class="buTton-containeR">
 <form action="/play6"> 
 <button type="submit" class="Center-button">3</button>
 </form>
 
    </div>


  <div class="buttOn-containeR">
 <form action="/play6"> 
 <button type="submit" class="Center-button">4</button>
 </form>
 
    </div>



  <div class="buttoN-containeR">
 <form action="/play6"> 
 <button type="submit" class="Center-button">5</button>
 </form>

    </div>


<h7> BADDDD </h7>
<h8> NEUTRAL</h8>
<p> G000DD </p>
     <h9>By-Anshul Laxane</h9>


    
<div class="BUTTON-container">
 <button onclick="location.reload()" class="center-button">Get Random Street View</button>

 </div>
 
</body>
</html>

"""
play_P6="""
 <!DOCTYPE html>
<html>
<head>
    <title>GAME Page</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
     #street-view {
            width: 70%;
            height: 70vh; /* Full screen */
            border: none;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);     
        }
        #message { 
        
        color: white; font-weight: bold; 
        position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);   
        }
        
    body{
            background-image: url("{{ url_for('static', filename='retro.jpg') }}");
    
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color:black;
            font-family: 'Press Start 2P', cursive;
            margin: 0;
            height: 100vh;
            position: relative;

}
h1{


text-align: center;

}
h3{
color:Lime;
text-align: center;
font-size:15px;
position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h4{
color:black;
font-size:30
text-align:center;
font-weight: bold;
position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
}



h7{

color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 102.5%;
            left: 35%;
            transform: translate(-50%, -50%);
}
p{
color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 100%;
            left: 65%;
            transform: translate(-50%, -50%);
}
h8{
color:white;
font-weight:bold;
position: absolute;
            top: 101.5%;
            left: 50%;
            transform: translate(-50%, -50%);

}
h9{
color:orange;
font-size:10;
position: absolute;
            top: 102.5%;
            left: 10%;
            transform: translate(-50%, -50%);



}
  .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-containeR {
            position: absolute;
            top: 85%;
            left: 30%;
            transform: translate(-50%, -50%);                           
        }
        .button-container {
            
            position: absolute;
            top: 85%;
            left: 70%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 10px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .Center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        .Center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
.Center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
 .Button-containeR {
            position: absolute;
            top: 95%;
            left: 35%;
            transform: translate(-50%, -50%);                           
        }

 .bUtton-containeR {
            position: absolute;
            top: 95%;
            left: 40%;
            transform: translate(-50%, -50%);                           
        }


 .buTton-containeR {
            position: absolute;
            top: 95%;
            left: 50%;
            transform: translate(-50%, -50%);                           
        }


 .buttOn-containeR {
            position: absolute;
            top: 95%;
            left: 60%;
            transform: translate(-50%, -50%);                           
        }
        .BUTTON-container{
position: absolute;
            top: 50%;
            left: 92%;
            transform: translate(-50%, -50%);   
            
        }



 .buttoN-containeR {
            position: absolute;
            top: 95%;
            left: 65%;
            transform: translate(-50%, -50%);                           
        }
        
    </style>
</head>
<body>

<script>
    function changeColor(btn) {
        btn.style.background = "orange"; // Change to orange when clicked
        btn.style.color = "white"; // Optional: Change text color for better visibility
    }
</script>




<div id="street-view"></div>
 <h3 id="message"></h3>
    <script>
    let panorama;
       function loadRandomStreetview() {
    // Define India's latitude & longitude range
    // Generate a random lat/lng
    const lngMin = 80.18, lngMax = 80.31; //  CHENNAI City 
    const latMin = 12.89, latMax =13.15;   // 

    const randomLat = latMin + Math.random() * (latMax - latMin);
    const randomLng = lngMin + Math.random() * (lngMax - lngMin);

    const messageContainer = document.getElementById("message");
    const streetViewService = new google.maps.StreetViewService();
    const streetViewContainer = document.getElementById("street-view");
    const randomLocation = { lat: randomLat, lng: randomLng };
    streetViewService.getPanorama({ location: randomLocation, radius: 50 }, (data, status) => {
               
        if (status === "OK" && data.location.pano) {
            messageContainer.innerHTML = "";
        panorama = new google.maps.StreetViewPanorama(streetViewContainer, {
              pano: data.location.pano,
              pov: { heading: 270, pitch: 0 },
             zoom: 1
        });


    } else {
                    console.log("No movable Street View found, trying again...");
                    messageContainer.innerHTML = "No movable Street View found, trying again...";
                    loadRandomStreetView(); // Retry if the location isn't navigable
                }
            });
        }

    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE&callback=loadRandomStreetview" async defer></script>

 
    <h1>Find Trash In Indian Cities.</h1>

    <h3>City: Chennai</h3>


    
   <div class="button-containeR">
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">YES</button> 
 </div>
 
   <div class="button-container">
 
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">NO</button>
    </div>


  <div class="Button-containeR">
 <form action="/play7"> 
 <button type="submit" class="Center-button">1</button>
 </form>
    </div>

  <div class="bUtton-containeR">
 <form action="/play7"> 
 <button type="submit" class="Center-button">2</button>
 </form>
 
    </div>

  <div class="buTton-containeR">
 <form action="/play7"> 
 <button type="submit" class="Center-button">3</button>
 </form>
 
    </div>


  <div class="buttOn-containeR">
 <form action="/play7"> 
 <button type="submit" class="Center-button">4</button>
 </form>
 
    </div>



  <div class="buttoN-containeR">
 <form action="/play7"> 
 <button type="submit" class="Center-button">5</button>
 </form>

    </div>


<h7> BADDDD </h7>
<h8> NEUTRAL</h8>
<p> G000DD </p>
     <h9>By-Anshul Laxane</h9>


    
<div class="BUTTON-container">
 <button onclick="location.reload()" class="center-button">Get Random Street View</button>

 </div>
 
</body>
</html>
"""

play_P7="""
 <!DOCTYPE html>
<html>
<head>
    <title>GAME Page</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
     #street-view {
            width: 70%;
            height: 70vh; /* Full screen */
            border: none;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);     
        }
        #message { 
        
        color: white; font-weight: bold; 
        position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);   
        }
        
    body{
    
            background-image: url("{{ url_for('static', filename='retro.jpg') }}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color:black;
            font-family: 'Press Start 2P', cursive;
            margin: 0;
            height: 100vh;
            position: relative;

}
h1{


text-align: center;

}
h3{
color:Lime;
text-align: center;
font-size:15px;
position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h4{
color:black;
font-size:30
text-align:center;
font-weight: bold;
position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
}



h7{

color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 102.5%;
            left: 35%;
            transform: translate(-50%, -50%);
}
p{
color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 100%;
            left: 65%;
            transform: translate(-50%, -50%);
}
h8{
color:white;
font-weight:bold;
position: absolute;
            top: 101.5%;
            left: 50%;
            transform: translate(-50%, -50%);

}
h9{
color:orange;
font-size:10;
position: absolute;
            top: 102.5%;
            left: 10%;
            transform: translate(-50%, -50%);



}
  .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-containeR {
            position: absolute;
            top: 85%;
            left: 30%;
            transform: translate(-50%, -50%);                           
        }
        .button-container {
            
            position: absolute;
            top: 85%;
            left: 70%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 10px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .Center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        .Center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
.Center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
 .Button-containeR {
            position: absolute;
            top: 95%;
            left: 35%;
            transform: translate(-50%, -50%);                           
        }

 .bUtton-containeR {
            position: absolute;
            top: 95%;
            left: 40%;
            transform: translate(-50%, -50%);                           
        }


 .buTton-containeR {
            position: absolute;
            top: 95%;
            left: 50%;
            transform: translate(-50%, -50%);                           
        }


 .buttOn-containeR {
            position: absolute;
            top: 95%;
            left: 60%;
            transform: translate(-50%, -50%);                           
        }
        .BUTTON-container{
position: absolute;
            top: 50%;
            left: 92%;
            transform: translate(-50%, -50%);   
            
        }



 .buttoN-containeR {
            position: absolute;
            top: 95%;
            left: 65%;
            transform: translate(-50%, -50%);                           
        }
        
    </style>
</head>
<body>

<script>
    function changeColor(btn) {
        btn.style.background = "orange"; // Change to orange when clicked
        btn.style.color = "white"; // Optional: Change text color for better visibility
    }
</script>



<div id="street-view"></div>
 <h3 id="message"></h3>
    <script>
    let panorama;
       function loadRandomStreetview() {
    // Define India's latitude & longitude range
    // Generate a random lat/lng
    const lngMin =77.50, lngMax = 77.72; //  BANGALORE City 
    const latMin = 12.90, latMax =13.10;   // 

    const randomLat = latMin + Math.random() * (latMax - latMin);
    const randomLng = lngMin + Math.random() * (lngMax - lngMin);

    const messageContainer = document.getElementById("message");
    const streetViewService = new google.maps.StreetViewService();
    const streetViewContainer = document.getElementById("street-view");
    const randomLocation = { lat: randomLat, lng: randomLng };
    streetViewService.getPanorama({ location: randomLocation, radius: 50 }, (data, status) => {
               
        if (status === "OK" && data.location.pano) {
            messageContainer.innerHTML = "";
        panorama = new google.maps.StreetViewPanorama(streetViewContainer, {
              pano: data.location.pano,
              pov: { heading: 270, pitch: 0 },
             zoom: 1
        });


    } else {
                    console.log("No movable Street View found, trying again...");
                    messageContainer.innerHTML = "No movable Street View found, trying again...";
                    loadRandomStreetView(); // Retry if the location isn't navigable
                }
            });
        }

    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE&callback=loadRandomStreetview" async defer></script>

 
    <h1>Find Trash In Indian Cities.</h1>

    <h3>City: Bangalore</h3>
    <h4>TRASH </h4>

    
   <div class="button-containeR">
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">YES</button> 
 </div>
 
   <div class="button-container">
 
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">NO</button>
    </div>


  <div class="Button-containeR">
 <form action="/play8"> 
 <button type="submit" class="Center-button">1</button>
 </form>
    </div>

  <div class="bUtton-containeR">
 <form action="/play8"> 
 <button type="submit" class="Center-button">2</button>
 </form>
 
    </div>

  <div class="buTton-containeR">
 <form action="/play8"> 
 <button type="submit" class="Center-button">3</button>
 </form>
 
    </div>


  <div class="buttOn-containeR">
 <form action="/play8"> 
 <button type="submit" class="Center-button">4</button>
 </form>
 
    </div>



  <div class="buttoN-containeR">
 <form action="/play8"> 
 <button type="submit" class="Center-button">5</button>
 </form>

    </div>


<h7> BADDDD </h7>
<h8> NEUTRAL</h8>
<p> G000DD </p>
     <h9>By-Anshul Laxane</h9>


    
<div class="BUTTON-container">
 <button onclick="location.reload()" class="center-button">Get Random Street View</button>

 </div>
 
</body>
</html>
"""
play_P8="""
 <!DOCTYPE html>
<html>
<head>
    <title>GAME Page</title>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
     #street-view {
            width: 70%;
            height: 70vh; /* Full screen */
            border: none;
             position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);     
        }
        #message { 
        
        color: white; font-weight: bold; 
        position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);   
        }
        
    body{
    
            background-image: url("{{ url_for('static', filename='retro.jpg') }}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            color:black;
            font-family: 'Press Start 2P', cursive;
            margin: 0;
            height: 100vh;
            position: relative;

}
h1{


text-align: center;

}
h3{
color:Lime;
text-align: center;
font-size:15px;
position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h4{
color:black;
font-size:30
text-align:center;
font-weight: bold;
position: absolute;
            top: 75%;
            left: 50%;
            transform: translate(-50%, -50%);
}

h5{
color:yellow;
text-align:center;
font-size:15;
font-weight: bold;

}

h7{

color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 102.5%;
            left: 35%;
            transform: translate(-50%, -50%);
}
p{
color:white;
font-size:25;
font-weight:bold;
position: absolute;
            top: 100%;
            left: 65%;
            transform: translate(-50%, -50%);
}
h8{
color:white;
font-weight:bold;
position: absolute;
            top: 101.5%;
            left: 50%;
            transform: translate(-50%, -50%);

}
h9{
color:orange;
font-size:10;
position: absolute;
            top: 102.5%;
            left: 10%;
            transform: translate(-50%, -50%);



}
  .container {
            display: grid;
            place-items: center;
            height: 20vh;
        }
            
                .button-containeR {
            position: absolute;
            top: 85%;
            left: 30%;
            transform: translate(-50%, -50%);                           
        }
        .button-container {
            
            position: absolute;
            top: 85%;
            left: 70%;
            transform: translate(-50%, -50%);
        }
         .center-button 
         {
            padding: 10px 20px;
            font-size: 10px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .Center-button 
         {
            padding: 10px 20px;
            font-size: 30px;
            box-shadow: 5px 5px black;
              font-weight: bolder;
            color: black;
              background-color: #339999;
              font-family: cursive;
              border: 3px solid black;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.25s;
            display: inline-block;
        }
        .center-button:hover 
        {
            background-color: #be7079;
        }
        .Center-button:hover 
        {
            background-color: #be7079;
        }
        
        .center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
.Center-button:active {
    box-shadow: 0px 0px black;
    transform: translate(5px, 5px);
    
}
 .Button-containeR {
            position: absolute;
            top: 95%;
            left: 35%;
            transform: translate(-50%, -50%);                           
        }

 .bUtton-containeR {
            position: absolute;
            top: 95%;
            left: 40%;
            transform: translate(-50%, -50%);                           
        }


 .buTton-containeR {
            position: absolute;
            top: 95%;
            left: 50%;
            transform: translate(-50%, -50%);                           
        }


 .buttOn-containeR {
            position: absolute;
            top: 95%;
            left: 60%;
            transform: translate(-50%, -50%);                           
        }
        .BUTTON-container{
position: absolute;
            top: 50%;
            left: 92%;
            transform: translate(-50%, -50%);   
            
        }



 .buttoN-containeR {
            position: absolute;
            top: 95%;
            left: 65%;
            transform: translate(-50%, -50%);                           
        }
        
    </style>
</head>
<body>

<script>
    function changeColor(btn) {
        btn.style.background = "orange"; // Change to orange when clicked
        btn.style.color = "white"; // Optional: Change text color for better visibility
    }
</script>



<div id="street-view"></div>
 <h3 id="message"></h3>
    <script>
    let panorama;
       function loadRandomStreetview() {
    // Define India's latitude & longitude range
    // Generate a random lat/lng
    const lngMin = 85.05, lngMax = 85.25; //  SRINAGAR City 
    const latMin = 25.57, latMax =25.65;   // 

    const randomLat = latMin + Math.random() * (latMax - latMin);
    const randomLng = lngMin + Math.random() * (lngMax - lngMin);

    const messageContainer = document.getElementById("message");
    const streetViewService = new google.maps.StreetViewService();
    const streetViewContainer = document.getElementById("street-view");
    const randomLocation = { lat: randomLat, lng: randomLng };
    streetViewService.getPanorama({ location: randomLocation, radius: 50 }, (data, status) => {
               
        if (status === "OK" && data.location.pano) {
            messageContainer.innerHTML = "";
        panorama = new google.maps.StreetViewPanorama(streetViewContainer, {
              pano: data.location.pano,
              pov: { heading: 270, pitch: 0 },
             zoom: 1
        });


    } else {
                    console.log("No movable Street View found, trying again...");
                    messageContainer.innerHTML = "No movable Street View found, trying again...";
                    loadRandomStreetView(); // Retry if the location isn't navigable
                }
            });
        }

    </script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD9Io9GsANMd-eSBvbSOVX7Jsvg5WAXQRE&callback=loadRandomStreetview" async defer></script>

 
    <h1>Find Trash In Indian Cities.</h1>

    <h3>City: Patna</h3>
    <h4>TRASH </h4>
    
   <div class="button-containeR">
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">YES</button> 
 </div>
 
   <div class="button-container">
 
 <button type="submit" class="center-button" class="retro-button" onclick="changeColor(this)">NO</button>
    </div>


  <div class="Button-containeR">
 <form action="/play9"> 
 <button type="submit" class="Center-button">1</button>
 </form>
    </div>

  <div class="bUtton-containeR">
 <form action="/play9"> 
 <button type="submit" class="Center-button">2</button>
 </form>
 
    </div>

  <div class="buTton-containeR">
 <form action="/play9"> 
 <button type="submit" class="Center-button">3</button>
 </form>
 
    </div>


  <div class="buttOn-containeR">
 <form action="/play9"> 
 <button type="submit" class="Center-button">4</button>
 </form>
 
    </div>



  <div class="buttoN-containeR">
 <form action="/play9"> 
 <button type="submit" class="Center-button">5</button>
 </form>

    </div>


<h7> BADDDD </h7>
<h8> NEUTRAL</h8>
<p> G000DD </p>
     <h9>By-Anshul Laxane</h9>


    
<div class="BUTTON-container">
 <button onclick="location.reload()" class="center-button">Get Random Street View</button>

 </div>
 
</body>
</html>

"""
play_P9="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Over</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

       
        body {  background-image: url("{{ url_for('static', filename='noob.gif') }}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: black;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: black;
            font-family: 'Press Start 2P', cursive;
            text-align: center;
            overflow: hidden;
        }

        .crt {
            position: absolute;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.2);
            animation: scanlines 1s linear infinite;
            pointer-events: none;
        }

        @keyframes scanlines {
            0% { background: rgba(0, 0, 0, 0.1); }
            50% { background: rgba(0, 0, 0, 0.2); }
            100% { background: rgba(0, 0, 0, 0.1); }
        }

        .game-over {
            font-size: 50px;
            text-shadow: 4px 4px 0px  #ff0000, -4px -4px 0px #000000;
            animation: flicker 1s infinite alternate;
        }

        @keyframes flicker {
            0% { opacity: 1; }
            50% { opacity: 0.8; }
            100% { opacity: 1; }
        }

        .message {
            font-size: 18px;
            color:white;
            margin-top: 20px;
            animation: blink 1s infinite alternate;
        }

        @keyframes blink {
            0% { opacity: 1; }
            100% { opacity: 0.3; }
        }

        .try-again {
            margin-top: 30px;
            padding: 15px 30px;
            font-size: 18px;
            color: #ff5050;
            background: black;
            border: 3px solid #00ff00;
            cursor: pointer;
            font-family: 'Press Start 2P', cursive;
            text-transform: uppercase;
            text-shadow: 2px 2px 0px #000;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .try-again:hover {
            transform: scale(1.1);
            box-shadow: 0px 0px 10px #ff0000;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="game-over">GAME OVER</div>
    <div class="message">Insert Coin to Continue...</div>
    <button class="try-again" onclick="restartGame()">Try Again</button>
</div>

<div class="crt"></div> <!-- CRT effect overlay -->

<script>
    function restartGame() {
        window.location.href = "/"; // Redirect to the home page
    }
</script>

</body>
</html>



"""
@app.route('/')
def home():
    return render_template_string(home_P)
@app.route('/next')
def next():
    return render_template_string(next_P)
@app.route('/game')
def game():
    username = request.args.get('username', 'Guest')
    return render_template_string(content_P, username=username)
@app.route('/play1')
def play1():
    username = request.args.get('username', 'Guest')
    return render_template_string(play_P1,username=username ,api_key=GOOGLE_MAPS_API_KEY)
@app.route('/play2')
def play2():
    username = request.args.get('username', 'Guest')
    return render_template_string(play_P2,username=username ,api_key=GOOGLE_MAPS_API_KEY)

@app.route('/play3')
def play3():
    username = request.args.get('username', 'Guest')
    return render_template_string(play_P3,username=username ,api_key=GOOGLE_MAPS_API_KEY)

@app.route('/play4')
def play4():
    username = request.args.get('username', 'Guest')
    return render_template_string(play_P4,username=username ,api_key=GOOGLE_MAPS_API_KEY)

@app.route('/play5')
def play5():
    username = request.args.get('username', 'Guest')
    return render_template_string(play_P5,username=username ,api_key=GOOGLE_MAPS_API_KEY)

@app.route('/play6')
def play6():
    username = request.args.get('username', 'Guest')
    return render_template_string(play_P6,username=username ,api_key=GOOGLE_MAPS_API_KEY)

@app.route('/play7')
def play7():
    username = request.args.get('username', 'Guest')
    return render_template_string(play_P7,username=username ,api_key=GOOGLE_MAPS_API_KEY)

@app.route('/play8')
def play8():
    username = request.args.get('username', 'Guest')
    return render_template_string(play_P8,username=username ,api_key=GOOGLE_MAPS_API_KEY)

@app.route('/play9')
def play9():
    return render_template_string(play_P9)
def run_flask(): 
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)

# Start the Flask app in a separate thread
thread = threading.Thread(target=run_flask)
thread.start()

# Open in browser automatically
webbrowser.open("http://127.0.0.1:5000")
