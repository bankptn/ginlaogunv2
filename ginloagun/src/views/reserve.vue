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
                <div class="res-layout">
                    <img src="../assets/Refeel ผังร้าน 2.svg" alt="">
                </div>
            </div>
            <div>
                <div class="book-form">
                    <form>
                        <h1 class="book">Book table</h1> 
                        
                        <div class="formfield">
                            <span class="form-label">First name</span>
                            <input class="form-control" type="text" placeholder="first name">
                        </div> 
                        <div class="formfield">
                            <span class="form-label">Last name</span>
                            <input class="form-control" type="text" placeholder="last name">
                        </div> 
                        <div class="formfield">
                            <span class="form-label">Email</span>
                            <input class="form-control" type="text" placeholder="email">
                        </div> 
                        <div class="formfield">
                            <span class="form-label">Phone number</span>
                            <input class="form-control" type="text" placeholder="082022xxxx">
                        </div> 
                        <div class="formfield">
                            <span class="form-label">Date</span>
                            <input class="form-control" type="date" required>
                        </div> 
                        <div class="formfield">
                            <span class="form-label">Time</span>
                            <input class="form-control" type="time" required>
                        </div> 
                        <div class="formfield">
                            <span class="form-label">Table</span>
                            <input class="form-control" type="text" placeholder="Axx,Bxx,Cxx,Dxx" required>
                        </div> 
                        <div class="button">
                            <button class="submit">Submit</button>
                            <button class="cancel">Cancel</button>
                        </div>    
                    </form>
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

    --submitbtn-color: #8AD450;
    --cancelbtn-color: #FF3535;
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

/* .cusname a {
    text-decoration: none;
    color: #ffffff;
    font-size: 18px;
    position: relative;
    right: -10px;
} */

/* .desktop-nav .menu-item li a.signin-btn {
    color: #000000;
}
.desktop-nav .menu-item li a.signup-btn {
    color: #000000;
} */

/* a.signin-btn {
    background: var(--signinbtn-color);
    color: #000000;
    border-radius: 50px;
    padding: 15px 13px;
}
a.signup-btn {
    background: var(--signupbtn-color);
    color: #000000;
    border-radius: 50px;
    padding: 15px 13px;
} */



.container1 {
    margin-top: 68px;
    margin-left: 50px;
    
    display: grid;
    grid-template-columns: 40% 60%;
    width: 1420px;
    height: 840px;
    

    background: #434343;
    border-radius: 20px;
}

/* ผังร้าน */
.res-layout {
    margin-top: 80px;
    margin-left: 20px;
    width: 840px;
    height: 480px;
}

/* Book form */
.book-form {
    margin: auto;
    color: #ffffff;
    padding: 50px 20px;
    margin-right: 10px;
    margin-top: 50px;
    width: 420px;
    border-radius: 20px;
}

form {
    display: grid;
    grid-row-gap: 25px;
    justify-content: space-between;
}

.book-form h1 {
    font-size: 64px;
    justify-content: center;
}

.book {
    display: grid;
    grid-row-gap: 100px;
}

.book-form .form-label {
    font-size: 20px;
    display: inline-block;

}



.book-form .formfield {
    position: relative;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    
}

.formfield p {
    font-size: 20px;
}

.book-form .form-control {
    display: inline-flex;
    justify-content: space-between;
    background-color: #ebecee;
    border-radius: 4px;
    border: none;
    height: 30px;
    -webkit-box-shadow: none ;
    box-shadow: none;
    font-size: 14px;
}




.button .submit {
    display: inline-block;
    background-color: var(--submitbtn-color);
    font-size: 20px;
    padding: 14px 30px;
    border-radius: 50px;
    margin-left: 10px;
    font-weight: 700;
    border: none;
    -webkit-transition: 0.2s all;
    transition: 0.2s all;
}

.button .cancel {
    display: inline-block;
    background-color: var(--cancelbtn-color);
    font-size: 20px;
    padding: 14px 30px;
    border-radius: 50px;
    margin-left: 50px;
    font-weight: 700;
    border: none;
    -webkit-transition: 0.2s all;
    transition: 0.2s all;
}

.book-form .submit:hover,
.book-form .submit:focus {
	opacity: 0.7;
}

.book-form .cancel:hover,
.book-form .cancel:focus {
	opacity: 0.7;
}
</style>