<template>
  <header>
        <nav>
            <div class="bar"></div>
        </nav>
        <div class="wrapper">
            <nav class="desktop-nav">
                <div class="logo">
                    <a href="#">
                        <img id="logo-click" src="../assets/Logo-3.svg" alt="">
                    </a>
                    
                </div>
    
                <div class="nav">
                    <a href="#" id="home" class="active">Home</a>
                    <div class="dropdown">
                        <button class="rdropbtn">Restaurants
                            <i class="resdown"></i>
                        </button>
                        <div class="dropdown-res">
                            <a href="#" id="red">Refeel Bar & Bistro</a>
                            <a href="#" id="cd">C - minor</a>
                            <a href="#" id="zynd">Zyn music bar & hashery</a>
                            <a href="#" id="2getd">2gether bar & restaurant</a>
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
                        <a href="#" id="profile">Profile</a>
                        <a href="#" id="edit">Edit profile</a>
                        <a href="#" id="logout">Sign out</a>
                    </div>
                </div>
            </nav>
        </div>  
        <div class="container">
            <!-- <div class="logo">
                <div class="navlogo"></div>
                <a href="#">
                    <img src="{% static 'img/Group 9.svg' %}" alt="GinLaoGun" width="450" height="100">
                </a>
            </div> -->
            <section class="background">
                <br>
                <section class="top">
                    <h2>Profile</h2>
                        <a href="#">
                            <img src="../assets/user 1.svg" alt="Profile Picture" width="115" height="115">
                        </a>
                </section>
                <section class="top2">
                    <h2>Add Profile Picture</h2>
                </section>
                <section class="name">
                    <div class="name-title">
                        <h1>Name</h1>
                        <input type='text' id='txt_Name' name='name' class='form-control' placeholder='Name' readonly>
                    </div>
                    <div class="lastname-title">
                        <h1>Last Name</h1>
                        <input type='text' id='txt_LastName' name='lastname' class='form-control' placeholder='Last Name' readonly>
                    </div>
                    <div class="id-title">
                        <h1>ID Card Number</h1>
                        <input type='text' maxlength="13" id='txt_Id' name='id' class='form-control' placeholder='ID Card Number' readonly>
                    </div>
                </section>
                <br>
                <section class="birth">
                    <div class="birth-title">
                        <h1>Date of Birth</h1>
                        <input type='text' name='date' class='form-control' placeholder='Date of birth' readonly>
                    </div>
                    <div class="address-title">
                        <h1>Address</h1>
                        <input type='text' id='txt_Address' name='address' class='form-control' placeholder='Address' readonly>
                    </div>       
                    <div class="tel-title">
                        <h1>Tel.</h1>
                        <input type='text' maxlength="10" id='txt_Tel' name='tel' class='form-control' placeholder='Tel.' readonly>
                    </div>
                </section>
                <br>
                <section class="mail">
                    <div class="mail-title">
                        <h1>E-mail</h1>
                        <input type='text' id='txt_Mail' name='mail' class='form-control' placeholder='E-Mail' readonly>
                    </div>
                    <div class="user-title">
                        <h1>Username</h1>
                        <input type='text' id='txt_User' name='user' class='form-control' placeholder='Username' readonly>
                    </div>
                    <div class="pass-title">
                        <h1>Password</h1>
                        <input type='password' id='txt_Pass' name='pass' class='form-control' placeholder='Password' readonly>
                    </div>
                    </section>
                <br>
                <section>
                    <div class="btn">
                        <div class="edit-btn">
                            <a href="#" id="edit-profile" class="cancel">Edit Profile</a>
                        </div>
                        <div class="home-btn">
                            <a href="#" id="home" class="home">Home</a>
                        </div>
                    </div>
                </section>
            </section>

        </div>
    </header>
</template>

<script>
export default {

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Roboto', sans-serif;
}

/* Colors */

:root {
    --darkbrown-color: #2C2626;
    --lightbrown-color: #434343;
    --lightgray-color: #C4C4C4;

    --signinbtn-color: #A3DD80;
    --signupbtn-color: #BE6C6C;

    --blackhover-color: #000000;
}

.container {
    max-width: 1520px;
    max-height: 740px;
    margin: 0 auto;
}

header {
    width: 1536px;
    height: 753px;
    background: url(../assets/home.svg) no-repeat;
}

/* .bar {
    height: 20px;
} */

/* .logo .navlogo {
    height: 8px;
} */

/* .logo {
    margin-top: 0px;
    margin-left: 518px;
    width: 500px;
    height: 120px;
    left: 629px;
    top: 38px;

    background: #454545;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 50px;
}

.logo a {
    margin-left: 25px;
} */

.background {
    margin-top: 50px;
    margin-left: 117.5px;
    
    width: 1275px;
    height: 575px;
    left: 168px;
    top: 247px;
    /* border: 1px solid red; */
    /* display: flex; */

    background: #454545;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.5);
    border-radius: 20px;
}

.name-title {
    margin-left: 50px;
}

.name-title input {

    width: 300px;
    height: 60px;
    left: 205px;
    top: 525px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.lastname-title input {
    width: 300px;
    height: 60px;
    left: 616px;
    top: 525px;
    
    /* margin-right: 100px; */
    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.id-title input {
    margin-right: 50px;

    width: 500px;
    height: 60px;
    left: 1027px;
    top: 525px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.birth-title {
    margin-left: 50px;
}

.birth-title input {
    width: 300px;
    height: 60px;
    left: 205px;
    top: 684px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.address-title input {
    width: 500px;
    height: 60px;
    left: 607px;
    top: 684px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.tel-title input {
    width: 300px;
    height: 60px;
    left: 1297px;
    top: 684px;
    
    margin-right: 50px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.mail-title {
    margin-left: 50px;
}

.mail-title input {
    width: 300px;
    height: 60px;
    left: 200px;
    top: 843px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.user-title input {
    width: 300px;
    height: 60px;
    left: 611px;
    top: 843px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.pass-title input {
    width: 235px;
    height: 60px;
    left: 1032px;
    top: 843px;

    font-size: 25px;
    margin-right: 315px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

/* .repass-title input {
    width: 235px;
    height: 60px;
    left: 1032px;
    top: 843px;

    font-size: 25px;

    margin-right: 50px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
} */


/* .cancel-btn a {

    text-align: center;
    width: 200px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;

    margin-top: 10px;
    margin-left: 800px;

    background: #ED8C8C;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 50px;
    color: black;
    text-decoration: none;
    display: inline-block;
    font-size: 36px;
} */

.edit-btn a{
    text-align: center;
    width: 200px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;

    margin-top: 10px;
    margin-left: 800px;

    background: #0c96e6;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 50px;
    color: black;
    text-decoration: none;
    display: inline-block;
    font-size: 36px;
}

.home-btn a {

    text-align: center;
    width: 200px;
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;

    margin-top: 10px;
    margin-left: 20px;

    background: #09aa31;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 50px;
    color: black;
    text-decoration: none;
    display: inline-block;
    font-size: 36px;
}

.btn {
    display: flex;
}


.name {
    display: flex;
    justify-content: space-between;
}

.birth {
    display: flex;
    justify-content: space-between;
}

.mail {
    display: flex;
    justify-content: space-between;
}

.top {
    margin-left: 47.5px;
    text-decoration: none;
    
    color: white;
    display: flex;
    
}

.top2 {
    margin-left: 47.5px;
    text-decoration: none;
    font-size: 12px;
    color: white;
    align-items: left;
    text-align: left;
    
    margin-left: 1069px;
}

.background h1 {
    color: white;
}

.top a {
    width: 130px;
    height: 130px;

    border-radius: 200px;
    margin-left: 877px;

    background: #C4C4C4;
    align-items: center;
    text-align: center;
    justify-content: center;
}

.top h2 {
    margin-top: 30px;
    font-size: 55px;
}

.desktop-nav {
    height: 85px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--darkbrown-color);
    padding: 2px 68px;

    
}

/* .desktop-nav .nav .menu-item {
    position: absolute;
    left: 950px;
    display: flex;
    list-style: none;
}

.desktop-nav .nav .menu-item {
    margin: 0 20px ;
}

.desktop-nav nav .menu-item a {
    text-decoration: none;
    color: #ffffff;
    font-size: 18px;
    position: relative;

}

.desktop-nav .nav .menu-item a.active::after {
    content: "";
    position: absolute;
    height: 5px;
    width: 100%;
    background: #ffffff;
    left: 0;
    top: -20px;
} */

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
</style>