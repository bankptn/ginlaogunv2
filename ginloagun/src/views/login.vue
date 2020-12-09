<template>
  <header>
        <nav>
            <div class="bar"></div>
        </nav>
        <div class="container">
            <div class="logo">
                <div class="navlogo"></div>
                <a href="#">
                    <img src="../assets/Group 9.svg" alt="GinLaoGun" width="500" height="100" id="bc">
                </a>
            </div>
            <section class="background">
                <section>
                    <br>
                    <section class="top">
                        <h2>Sign In</h2>
                    </section>
                    <br>
                    <!-- <form method="post">
                        {% csrf_token %}
                        {form} -->
                        <form id='form_login' action='/'>
                        <!-- {% csrf_token %} -->
                            <section class="username">
                                <div class="username-title">
                                    <h1>Username</h1>
                                </div>
                                <section class="usernamebox">
                                    <input type='text' id='txt_Username' name='username' class='form-control' placeholder='Username'>
                                </section>
                            </section>
                            <br>
                            <section class="password">
                                <div class="password-title">
                                    <h1>Password</h1>
                                </div>
                                <section class="passwordbox">
                                    <input type='password' id='txt_Password' name='password' class='form-control' placeholder='Password'>
                                </section>
                            </section>
                            <section>
                                <div class="create">
                                    <h1>New user?<a href="#" id="create">create an account</a></h1>
                                    
                                    <h1>Forget password?</h1>
                                </div>
                            </section>
                            <br>
                            <section>
                                <div class="signin-btn">
                                    <a href="#" id="signin-btn" class="signin">Sign In</a>
                                    
                                        <!-- <input type="submit" id="signin-btn" value="Sign In">
                                     -->
                                </div>
                            </section>
                        </form>
                    <!-- </form> -->
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
    height: 38px;
}

.logo .navlogo {
    height: 10px;
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

.background {
    margin-top: 30px;
    margin-left: 348px;
    width: 540px;
    
    width: 833px;
    height: 540px;
    left: 543px;
    top: 300px;
    /* border: 1px solid red; */
    display: flex;

    background: #454545;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.5);
    border-radius: 20px;
}

.usernamebox input{
    margin-top: 25px;
    margin-left: 47.5px;

    width: 740px;
    height: 66px;
    left: 590px;
    top: 489px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.passwordbox input{
    margin-top: 25px;
    margin-left: 47.5px;

    width: 740px;
    height: 66px;
    left: 590px;
    top: 489px;

    font-size: 25px;

    background: #FFFFFF;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
}

.username-title {
    margin-left: 47.5px;
    text-decoration: none;
    font-size: 36px;
    color: white;
    display: flex;
    align-items: center;
}

.password-title {
    margin-left: 47.5px;
    text-decoration: none;
    font-size: 36px;
    color: white;
    display: flex;
    align-items: center;
}

.top {
    margin-left: 47.5px;
    text-decoration: none;
    font-size: 36px;
    color: white;
    display: flex;
    align-items: center;
}

.create {
    display: flex;
    justify-content: space-between;
}

.create h1 {
    margin-left: 47.5px;
    text-decoration: none;
    font-size: 24px;
    color: white;
    display: flex;
    align-items: center;
}

.create a {
    margin-left: 47.5px;
    display: flex;
    align-items: center;
    font-size: 24px;
    line-height: 35px;
    text-decoration: none;

    color: #8DEF84;

    text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.signin-btn a{
    margin-left: 268px;

    text-align: center;
    width: 250px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    

    background: #95E7EE;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 50px;
    color: black;
    text-decoration: none;
    display: inline-block;
    font-size: 48px;
}
</style>