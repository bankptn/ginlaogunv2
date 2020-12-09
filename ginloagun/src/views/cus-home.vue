<template>
   <header>
        <div class="wrapper">
            <nav class="desktop-nav">
                <div class="logo">
                    <a href="#">
                        <img src="../assets/Logo-3.svg" alt="">
                    </a>
                    
                </div>

                <div class="nav">
                    <a href="#" class="active">Home</a>
                    <div class="dropdown">
                        <button class="rdropbtn">Restaurants
                            <i class="resdown"></i>
                        </button>
                        <div class="dropdown-res">
                            <a href="#">Refeel Bar & Bistro</a>
                            <a href="#">C - minor</a>
                            <a href="#">Zyn music bar & hashery</a>
                            <a href="#">2gether bar & restaurant</a>
                        </div>
                    </div>
                    <a href="#">About Us</a>
                </div>

                <div class="bgpic">
                    <div class="cuspic">
                        <img src="../assets/user 2.svg" alt="">
                    </div>
                </div>

                <div class="dropdown1">
                    <button class="cdropbtn">Customer
                        <i class="cusdown"></i>
                    </button>
                    <div class="dropdown-cus">
                        <a href="#">Profile</a>
                        <a href="#">Edit profile</a>
                        <a href="#">Sign out</a>
                    </div>
                </div>
            </nav>
        </div>    
            <!-- End of Desktop Navigation -->
        <div class="container1">
            <div> 
                <div class="container1-1">
                    <a href="#">
                        <div class="cardContainer1">
                            <h1 class="headTitleContainer1">Refeel Bar & Bistro</h1>
                        </div>
                        <div class="cardContainer3">
                            <h1 class="headTitleContainer3">Zyn music bar & hashery</h1>
                        </div>
                    </a>
                </div>
            </div>
            <div>
                <div class="container1-2">
                    <a href="#">
                        <div class="cardContainer2">
                            <h1 class="headTitleContainer2">C-minor</h1>
                        </div>
                            
                        <div class="cardContainer4">
                            <h1 class="headTitleContainer4">2gether bar & restaurant</h1>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </header>
</template>

<script>
export default {

}
</script>

<style>
/* Colors */

:root {
    --darkbrown-color: #2C2626;
    --lightbrown-color: #434343;
    --lightgray-color: #C4C4C4;

    --signinbtn-color: #A3DD80;
    --signupbtn-color: #BE6C6C;

    --blackhover-color: #000000;
}

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

* {

    margin: 0;
    box-sizing: border-box;  
}

header {
    height: 1075px;
    width: 1520px;
    background: url(../assets/home.svg) no-repeat;
    margin: 0 auto;
} 

body {
    font-family: 'Roberto', sans-serif;
    
}
.wrapper {
    width: 1520px;
    margin: 0 auto;
    padding: 0 auto;
}

/* Header - Navigation */

.desktop-nav {
    height: 85px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--darkbrown-color);
    padding: 2px 68px;

    
}



/* Dropdown Res */
.nav {
    /* float: left; */
    /* overflow: hidden; */
    background-color: var(--darkbrown-color);
    width: 330px;
    align-items: inherit;
    margin-left: 560px;
}

/* Link inside nav */
.nav  a {
    float: left;
    font-size: 18px;
    color: #ffffff;
    text-align: center;
    padding: 16px 18px;
    text-decoration: none;
    
}

/* Home active */
.nav  a.active::after {
    content: "";
    /* position: absolute; */
    height: 5px;
    width: 100%;
    background: #ffffff;
    left: 0;
    top: -20px;
}

/* Dropdown container */
.dropdown {
    float: left;
    overflow: hidden;
}

/* Dropdown btn */
.dropdown .rdropbtn {
    font-size: 18px;
    border: none;
    outline: none;
    color: #ffffff;
    padding: 14px 16px;
    background-color: inherit;
    font-family: inherit;
    margin: 0;
}

/* Add black bg color to nav */
.nav a:hover, .dropdown:hover .rdropbtn {
    background-color: var(--lightbrown-color);
    border-radius: 20px;
}

/* Dropdown content */
.dropdown-res {
    display: none;
    position: absolute;
    background-color: #dddddd;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    border-radius: 20px;
}

/* Link Inside Dropdown */
.dropdown-res a {
    float: none;
    color: #000000;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}

/* Add grey background color to dropdown */
.dropdown-res a:hover {
    background-color: var(--lightgray-color);
    border-radius: 20px;
}

/* Show dropdown menu on hover */
.dropdown:hover .dropdown-res {
    display: block;
}

.bgpic {
    
    margin-right: -20px; 
    width: 51px;
    height: 51px;
    background: #ffffff;
    border-radius: 50px;
    
}

.bgpic .cuspic {
    margin-top: 10px;
    margin-left: 10px;
}

/* Customer dropdown */
.dropdown1 {
    float: left;
    overflow: hidden;
}

/* Dropdown btn */
.dropdown1 .cdropbtn {
    font-size: 18px;
    border: none;
    outline: none;
    color: #ffffff;
    padding: 16px 18px;
    background-color: inherit;
    margin: 0px;
}

/* Add bg color to cus btn */
.dropdown1:hover .cdropbtn {
    background-color: var(--lightbrown-color) ;
    border-radius: 20px;
}

/* Dropdown content */
.dropdown-cus {
    display: none;
    position: absolute;
    background-color: #dddddd;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    border-radius: 20px;
}

/* Link inside Dropdown */
.dropdown-cus a {
    float: none;
    color: #000000;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
    
}

/* dropdown cus hover */
.dropdown-cus a:hover{
    background-color: var(--lightgray-color);
    border-radius: 20px;
}

/* Show menu on hover */
.dropdown1:hover .dropdown-cus {
    display: block;
}

.container1 {
    margin-top: 68px;
    margin-left: 150px;
    /* margin-right: 95px; */
    /* width: 540px; */
    display: flex;

    width: 1220px;
    height: 840px;
    /* left: 278px;
    top: 150px;  */

    background: #434343;
    border-radius: 20px;
}

.container1-1 .cardContainer1 {
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 350px;
    height: 252px;
    border-radius: 20px;
    margin-top: 112px;
    margin-left: 173.3px;
}

.headTitleContainer1 {
    height: 20%;
    width: 100%;
    border-radius: 20px;
    background-color: var(--lightgray-color);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    color: #000000;
}

.container1-2 .cardContainer2 {
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 350px;
    height: 252px;
    border-radius: 20px;
    margin-top: 112px;
    margin-left: 173.3px;
}

.headTitleContainer2 {
    height: 20%;
    width: 100%;
    border-radius: 20px;
    background-color: var(--lightgray-color);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    color: #000000;
}

.container1-1 .cardContainer3 {
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 350px;
    height: 252px;
    border-radius: 20px;
    margin-top: 112px;
    margin-left: 173.3px;
}

.headTitleContainer3 {
    height: 20%;
    width: 100%;
    border-radius: 20px;
    background-color: var(--lightgray-color);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    color: #000000;
}

.container1-2 .cardContainer4 {
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    width: 350px;
    height: 252px;
    border-radius: 20px;
    margin-top: 112px;
    margin-left: 173.3px;
}

.headTitleContainer4 {
    height: 20%;
    width: 100%;
    border-radius: 20px;
    background-color: var(--lightgray-color);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    color: #000000;
}

a {
    text-decoration: none;
}
</style>