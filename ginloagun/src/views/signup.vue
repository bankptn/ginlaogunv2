<template>
  <header>
        <nav>
            <div class="bar"></div>
        </nav>
        <div class="container">
            <div class="logo">
                <div class="navlogo"></div>
                <a href="#">
                    <img src="../assets/Group 9.svg" alt="GinLaoGun" width="450" height="100" id="bc">
                </a>
            </div>
            <section class="background">
                <br>
                <section class="top">
                    <h2>Sign Up</h2>
                        <a href="#">
                            <img src="../assets/user 1.svg" alt="Profile Picture" width="115" height="115">
                        </a>
                </section>
                <section class="top2">
                    <h2>Add Profile Picture</h2>
                </section>
                <form id='form_signup' action='/'>
                    <section class="name">
                        <div class="name-title">
                            <h1>Name</h1>
                            <input type='text' id='txt_Name' name='customer_name' class='form-control' placeholder='Name'>
                        </div>
                        <div class="lastname-title">
                            <h1>Last Name</h1>
                            <input type='text' id='txt_LastName' name='customer_lastname' class='form-control' placeholder='Last Name'>
                        </div>
                        <div class="id-title">
                            <h1>ID Card Number</h1>
                            <input type='text' maxlength="13" id='txt_Id' name='id_card' class='form-control' placeholder='ID Card Number'>
                        </div>
                    </section>
                    <br>
                    <section class="birth">
                        <div class="birth-title">
                            <h1>Date of Birth</h1>
                            <input type='text' id='txt_Bday' name='bday' class='form-control' placeholder='Date of birth'>
                            <!-- <div class="valid-feedback">Valid.</div>
                            <div class="invalid-feedback">Check this checkbox to continue.</div> -->
                            <!-- <button type='button' class="btn btn-default" id='btn_BirthDay'> -->
                                <span class="glyphicon glyphicon-calendar"></span>
                            <!-- </button> -->
                        </div>
                        <div class="address-title">
                            <h1>Address</h1>
                            <input type='text' id='txt_Address' name='address' class='form-control' placeholder='Address'>
                        </div>       
                        <div class="tel-title">
                            <h1>Tel.</h1>
                            <input type='text' maxlength="10" id='txt_Tel' name='tel' class='form-control' placeholder='Tel.'>
                        </div>
                    </section>
                    <br>
                    <section class="mail">
                        <div class="mail-title">
                            <h1>E-mail</h1>
                            <input type='text' id='txt_Mail' name='email' class='form-control' placeholder='E-Mail'>
                        </div>
                        <div class="user-title">
                            <h1>Username</h1>
                            <input type='text' id='txt_User' name='username' class='form-control' placeholder='Username'>
                        </div>
                        <div class="pass-title">
                            <h1>Password</h1>
                            <input type='password' id='txt_Pass' name='password' class='form-control' placeholder='Password'>
                        </div>
                        <div class="repass-title">
                            <h1>Re-Enter Password *</h1>
                            <input type='password' id='txt_RePass' name='repass' class='form-control' placeholder='Re-Password'>
                        </div>
                        </section>
                    <br>
                    <section>
                        
                        <div class="signup-btn" id="signup-btn">
                            <a href="#" class="signup">Sign Up</a>
                        </div>
                    </section>
                </form>
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

.bar {
    height: 20px;
}

.logo .navlogo {
    height: 8px;
}

.logo {
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
}

.background {
    margin-top: 25px;
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

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.repass-title input {
    width: 235px;
    height: 60px;
    left: 1032px;
    top: 843px;

    font-size: 25px;

    margin-right: 50px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.user-id input {
    width: 300px;
    height: 60px;
    left: 205px;
    top: 525px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.user-id {
    margin-left: 50px;
}


.signup-btn a {

    text-align: center;
    width: 250px;
    height: 75px;
    display: flex;
    align-items: center;
    justify-content: center;

    /* margin-top: -75px; */
    margin-left: 975px;

    background: #95E7EE;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 50px;
    color: black;
    text-decoration: none;
    display: inline-block;
    font-size: 45px;
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
    /* align-items: center; */
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
    margin-left: 852px;

    background: #C4C4C4;
    align-items: center;
    text-align: center;
    justify-content: center;
}

.top h2 {
    margin-top: 30px;
    font-size: 55px;
}


</style>