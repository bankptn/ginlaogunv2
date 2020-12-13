<template>
  <div>
    <v-app-bar color="#454545" permanent dark app>
      <v-toolbar-title>
        <router-link to="/">
          <v-img src="../../assets/Logo-3.svg"> </v-img
        ></router-link>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn text>
        <span @click="onClickHome">Home</span>
      </v-btn>

      <div class="dropdown">
        <v-btn text>
          <span>Restaurant</span>
        </v-btn>

        <div class="dropdown-res">
          <a href="/refeel"><span>Refeel Bar & Bistro</span></a>
          <a href="/refeel"><span>C - minor</span></a>
          <a href="/refeel"><span>Zyn music bar & hashery</span></a>
          <a href="/refeel"><span>2gether bar & restaurant</span></a>
        </div>
      </div>
      
      <v-btn text>
        <span>About Us</span>
      </v-btn>

      <div id="sign_in" style="margin: 10px">
        <v-btn @click="onClickSignIn" rounded color="success">sign in</v-btn>
      </div>

      <div id="sign_up" style="margin: 10px">
        <v-btn @click="onClickSignUp" rounded color="#BE6C6C">sign up</v-btn>
      </div>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data: () => ({
    items: ["Foo", "Bar", "Fizz", "Buzz"],
  }),
    methods: {
        onClickSignUp () {
            this.$router.push({name:"Signup"})
        },
        onClickSignIn () {
            this.$router.push({name:"login"})
        },
        onClickHome () {
            this.$router.push({name:"home"})
        },
        
    },
};
</script>

<style scoped>
.btnRestaurant {
  position: relative;
  display: inline-block;
}

.selectonHover {
  display: none;
  position: absolute;
  background-color: rgb(255, 255, 255);
  min-width: 135px;
  z-index: 1;
  border-radius: 10px;
}

.selectonHover a:hover {
  background-color: rgb(216, 216, 216);
  color: #fff;
}

.btnRestaurant:hover .selectonHover {
  display: block;
}

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

/* Dropdown content */
.dropdown-res {
  display: none;
  position: absolute;
  background-color: #dddddd;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
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
  background-color: #c4c4c4;
  border-radius: 20px;
}

/* Show dropdown menu on hover */
.dropdown:hover .dropdown-res {
  display: block;
}
</style>
