<template>
  <header>
       <div class="container">
           <nav>
               <ul>
                  <img src="../assets/beer1.svg">
                  <!-- <img src="beer1.svg"> -->
                  <p>Gin Lao Gun</p>
               </ul>
               <div class="nav-btn">
                   <a href="#" class="Home" id="home">Home</a>
                   <div class="Restaurant">
                     <button class="dropbtn1">Restaurant
                        <i class="fa fa-caret-down"></i>
                     </button>
                     <div class="dropdown-content1">
                        <a href="#" id="red">Refeel Bar & Bistro</a>
                        <a href="#" id="cd">C - minor</a>
                        <a href="#" id="zynd">Zyn music bar & hashery</a>
                        <a href="#" id="2getd">2gether bar & restaurant</a>
                     </div>
                  </div>
                  <a href="#" class="about_us">About Us</a>
                   <div class="BgUs">
                      <img src="../assets/user.svg">
                      <!-- <img class="User" src="user.svg"> -->
                   </div>
                   <div class="User1">
                     <button class="dropbtn2">User
                        <i class="fa fa-caret-down"></i>
                     </button>
                     <div class="dropdown-content2">
                        <a href="#">Profile</a>
                        <a href="#" id="edit">Edit profile</a>
                        <a href="#">Reservation history</a>
                        <a href="#">Sign out</a>
                     </div>    
                   </div>   
               </div>  
           </nav>
           
            <div class="Name">
               <p>2gether bar & restaurant</p>
            </div>
            
            <div class="Box"></div>
               <section class="Information">
                  <div class="In-title">
                     <p>Information</p>
                     
                  </div>
               </section>
               <section class="Promotion">
                  <div class="PR">
                     <p>Promotion</p>
                     
                  </div>
              </section>
              <section class="Menu">
                  <div class="Me">
                     <p>Menu</p>
                    
                  </div>
              </section>
              <section class="Review">
                  <div class="Re">
                     <p>Reviews</p>
                     <div class="BgRe">
                        <img src="../assets/user.svg">
                        <!-- <img class="Pic_Us" src="user.svg"> -->
                     </div>
                     <div class="img_re">
                        <div class="Rating">
                           <span id="rate_1"></span>
                           <span id="rate_2"></span>
                           <span id="rate_3"></span>
                           <span id="rate_4"></span>
                           <span id="rate_5"></span>
                        </div> 
                     </div>
                     <div class="ReSub">
                        <a href="#" class="Submit">Submit</a>
                     </div>
                 </div>
              </section>
              <section class="Band_Schedule">
                  <div class="BS">
                     <p>Band Schedule</p>
                  </div>
              </section>
              <section class="Table_available">
                  <div class="TA">
                     <nav2>
                     
                        <p>Table Available</p>
                        <div class ="image-ta">
                            <img src="../assets/Group.svg">
                        <!-- <img src="Group.svg"> -->
                        </div>
                        <div class="TBook">
                           <a href="#" class="Book">Book</a>
                        </div>
                     </nav2>
                 </div>
              </section>
       </div>
   </header>
</template>

<script>
export default {

}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Phetsarath', sans-serif;
}
.container {
    margin: 0 auto;
}

header{
    height: 1075px;
    width: 1520px;
    background: url(../assets/home.svg) no-repeat;
    margin-left: 250px;

}

nav {
    height : 85px;
    display: flex;
    justify-content: space-between;
    align-items:  center;
    list-style: none;
    background-color: #2C2626;
   
 }
 nav img{
     margin-top: -10px;
     margin-left: 40px;
     width: 40px;
     height: 40px;
     align-items:  center;

 }
 nav p{
     margin-left:90px;
     margin-top: -45px;
     align-items:  center;
 }

.Name{ 
    margin-top: 20px;
    text-align: center;
    height: 70px;
    display: inline-block;
    margin-left: 500px;
    
    
}
.Name p{
    font-size: 36px;
    color: #ffffff;
    height: 70px;
    align-items: center;
    border-radius: 50px;
    width: 500px;
    background-color: #2C2626;
    padding: .5rem 3rem;
    border: solid #ffffff 5px;
    background-repeat: no-repeat;
    background-clip: border-box;
}

.container nav ul p{
    font-size: 36px;
    color: #ffffff;
}
.Box{
    height: 920px;
    width: 1320px;
    margin-top: -30px;
    margin-left: 95px;
    background: #434343;
    border-radius: 10px;
}
.Information {
    margin-top: -860px;
    margin-left: 160px;
    background: #ffffff;
    border-radius: 20px;
    width: 550px;
    height: 260px;
}

.Promotion{
    margin-top: -255px;
    margin-left: 795px;
    background: #ffffff;
    border-radius: 20px;
    width: 550px;
    height: 360px;
}
.Menu{
    background: #ffffff;
    border-radius: 20px;
    margin-left: 160px;
    margin-top: -65px;
    width: 550px;
    height: 360px;
}
.Review{
    background: #ffffff;
    border-radius: 20px;
    margin-left: 795px;
    width:  550px;
    height: 280px;
    margin-top: -250px;
}
.Band_Schedule{
    background: #ffffff;
    border-radius: 20px;
    width: 550px;
    margin-left: 160px;
    height: 130px;
    margin-top: 10px;
}
.Table_available{
    background: #ffffff;
    border-radius: 20px;
    width:550px;
    margin-left: 795px;
    height: 90px;
    display: flex;
    justify-content: space-between;
    align-items:  center;
    list-style: none;
    margin-top: -100px;
}
.TBook a{
    background: #50B85B;
    padding:.25rem .75rem;
    border-radius:20px ;
    width: 60px;
    height: 30px;
    margin-left: 10px;

    text-decoration: none;
    color: black;

}
nav2 {
    display: flex;
    justify-content: space-between;
    align-items:  center;
    list-style: none;
}
.image-ta{
    margin-left: 260px;
}
.TA p{
    margin-left: 30px;
}
.BS p{
    margin-left: 30px;
    padding: 1rem;
}
.In-title{
    margin-left: 30px;
    padding: 1rem;
}
.Me{
    margin-left: 30px;
    padding: 1rem;
}
.PR{
    margin-left: 30px;
    padding: 1rem;
}
.Re p{
    margin-left: 30px;
    padding: 1rem;
}
.ReSub a{
    background: #50B85B;
    padding:.3rem 1.3rem;
    border-radius: 50px;
    width: 90px;
    height: 30px;
    margin-left: 420px;
    margin-top: -40px;

    text-decoration: none;
    color: black;

}
.But_img{
    background: none;
    width: 70px;
    height: 70px;
    padding:0.5px 0.5px;
}
.nav-btn .Drop{
    width: 15px;
    height: 15px;
    margin-right: 20px;
    margin-top: 5px;
    justify-content: space-between;

}
.img_re{
    margin-top: -65px;
    margin-left: 80px;
}


.Pic_Us{
    width: 40px;
    height: 40px;
    margin-left: 10px;
    margin-top: 10px;    
}
.BgRe{
    border: 2px solid black;
    width: 65px;
    height: 65px;
    border-radius: 50px;
    margin-top: 150px;
    margin-left: 70px;

}
.Rating {
    width: 150px;
    height: 100px;
    display: inline-block;
    display: inline;
    unicode-bidi: bidi-override;
    direction: rtl;
    vertical-align: middle;
    margin-left: 90px;
  }
  
  .Rating>span:before {
    content: '☆';
    color: #c7c5c5;
    height: 100px;
    width: 100px;
    cursor: pointer;
    font-size: 3em;
  }
  
  .Rating>span:hover:before,
  .Rating span:hover~span:before {
    color: rgb(0, 255, 42);
 }
.nav-btn{
   overflow: hidden;
   margin-right: 105px;
}
.nav-btn a {
   float: left;
   font-size: 18px;
   color: #ffffff;
   text-align: center;
   padding: 10px 10px;
   text-decoration: none;
}

.Restaurant {
   float: left;
   overflow: hidden;
  
   
}
.User1 {
   float: left;
   overflow: hidden;
   margin-left: 355px;
   margin-top: -50px;
}
.Restaurant .dropbtn1 {
    font-size: 18px;
    border: none;
    outline: none;
    color: white;
    padding: 8px 10px;
    background-color: inherit;
    font-family: inherit; /* Important for vertical align on mobile phones */
    margin: 0; /* Important for vertical align on mobile phones */
}
.User1 .dropbtn2 {
    font-size: 18px;
    border: none;
    outline: none;
    color: white;
    padding: 10px 10px;
    background-color: inherit;
    font-family: inherit; /* Important for vertical align on mobile phones */
    margin: 0; /* Important for vertical align on mobile phones */
}
.nav-btn a:hover, .Restaurant:hover .dropbtn1 {
    background-color: #c7c5c5;
    border-radius: 10px;
}
.nav-btn a:hover, .User1:hover .dropbtn2 {
    background-color: #c7c5c5;
    border-radius: 10px;
}
.dropdown-content1{
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 140px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    
}
.dropdown-content2 {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 140px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    
}
.dropdown-content1 a {
    float: none;
    color: black;
    padding:12px 16px;
    text-decoration: none;
    display: block;
    text-align: left;
}
.dropdown-content2 a {
    float: none;
    color: black;
    padding: 10px 10px;
    text-decoration: none;
    display: block;
    text-align: left;

}
.dropdown-content1 a:hover {
    background-color: #ddd;
}


.dropdown-content2 a:hover {
    background-color: #ddd;
}
.Restaurant:hover .dropdown-content1 {
    display: block;
    border-radius: 10px;
}
.User1:hover .dropdown-content2 {
    display: block;
    border-radius: 10px;
}
.Home {
    margin-right: 10px;
    padding-top: 0.5rem;

} 

.about_us{
    margin-right: 50px;
   
}
.dropbtn2{
    padding-bottom: 3rem;

}

.nav-btn{
    margin-top: 15px;
}
.Restaurant{
    padding : 1px 1px;
}
.BgUs{
    background: #ffffff;
    width: 50px;
    height: 50px;
    margin-left: 300px;
    border-radius: 50px ;
}  
.User{
    
    margin-left: 10px;
    margin-top: 10px;
    height: 30px;
    width: 30px;
}
</style>