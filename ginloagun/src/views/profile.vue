<template>
  <v-container fluid class="main" id="edit">
        <v-row justify="center" align="center">
          <v-row justify="center" align="center">
            <v-form
                class="cardBody"
                ref="form"
                v-model="valid"
                @submit.prevent="submitEdit"
                lazy-validation
            > 
            <div class="mainbg">
                <v-row> 
                    <v-col cols="6">
                        <h1>PROFILE</h1>
                    </v-col>
                    <v-col class="logoTitle" cols="6">
                        <div>
                            <v-card style="border-radius: 360px; min-width: 58px; min-height: 58px;">
                            <v-img
                                src="../assets/user 1.svg"
                                height="150px"
                                width="150px"
                                contain
                            />
                            </v-card>
                        </div>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="3">
                        <label>First Name</label>
                        <v-text-field
                            label="Regular"
                            placeholder="First Name"
                            v-model=account.fname
                            solo
                            readonly
                            name="fname"
                        />
                    </v-col>
                    <v-col cols="3">
                        <label>Last Name</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Last Name"
                            v-model=account.lname
                            solo
                            readonly
                            name="lname"
                        />
                    </v-col>
                    <v-col cols="6">
                        <label>ID Card Number</label>
                        <v-text-field
                            label="Regular"
                            placeholder="ID Card Number"
                            v-model=account.ssn
                            solo
                            readonly
                            name="ssn"
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4">
                        <label>Date of Birth</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Date of Birth"
                            v-model=account.birthDay
                            solo
                            readonly
                            name="birthDay"
                        />
                    </v-col>
                    <v-col cols="5">
                        <label>Address</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Address"
                            v-model=account.address
                            solo
                            readonly
                            name="address"
                        />
                    </v-col>
                    <v-col cols="3">
                        <label>Tel.</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Tel."
                            v-model=account.phoneNumber
                            solo
                            readonly
                            name="phoneNumber"
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="3">
                        <label>E-Mail</label>
                        <v-text-field
                            label="Regular"
                            placeholder="E-Mail"
                            v-model=account.email
                            solo
                            readonly
                            name="email"
                        />
                    </v-col>
                    <v-col cols="3">
                        <label>Username</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Username"
                            v-model=account.username
                            solo
                            readonly
                            name="username"
                        />
                    </v-col>
                    <!-- <v-col cols="3">
                        <label>Password</label>
                        <v-text-field
                            label="Regular"
                            type="password"
                            placeholder="Password"
                            solo
                            readonly
                        />
                    </v-col> -->
                    <!-- <v-col cols="3">
                        <label>Re-Enter Password</label>
                        <v-text-field
                            label="Regular"
                            type="password"
                            placeholder="Re-Enter Password"
                            solo
                            readonly
                        />
                    </v-col> -->
                </v-row>
                <v-row class="btn" justify="end" align="center">
                    <v-btn class="edit" style="background-color:  #0c96e6; border-radius: 20px;" @click="onClickEdit">
                        Edit Profile
                    </v-btn>
                    <v-btn class="home" style="background-color: #09aa31; border-radius: 20px;" @click="onClickHome">
                        Home
                    </v-btn>
                </v-row>
            </div>
            </v-form>
            
        </v-row>
        </v-row>
  </v-container>
</template>

<script>
import api from "../service/api"
import { server } from "../service/constants"
export default {
    name:"profile",
    methods: {
        onClickEdit () {
                this.$router.push({name:"edit"})
            },
        onClickHome () {
            this.$router.push({name:"home"})
        }
        },
    data() {
        return {
            account: 
            {
                ssn:"",
                fname:"",
                lanme:"",
                username:"",
                password:"",
                address:"",
                email:"",
                phoneNumber:"",
                birthDay:""
            },
            valid: true
        }
    },
    async mounted () {
        var userID = localStorage.getItem(server.USERNAME)
        var result = await api.reprofile(userID)
        console.log(result)
        if (result.data.status == "1") {
            this.account.ssn  = result.data.result.ssn
            this.account.fname  = result.data.result.fname
            this.account.lname  = result.data.result.lname
            this.account.username  = result.data.result.username
            this.account.password  = result.data.result.password
            this.account.address  = result.data.result.address
            this.account.email  = result.data.result.email
            this.account.phoneNumber  = result.data.result.phoneNumber
            this.account.birthDay  = result.data.result.birthDay
            

        }
    },
}
</script>

<style scoped>
.main {
    min-height: 100vh;
    background: url(../assets/home.svg);
    background-position: center;
    background-repeat: no-repeat;
    background-size: 145%;
}
.cardBody {
    min-width: 940px;
    margin-top: 10px;
    background-color: #454545;
    border-radius: 30px;
    padding: 20px;
    /* height: 60vh;
    width: 80vw; */
}

.logoTitle{
    display: flex;
    justify-content: flex-end;
}

.edit {
    background: #ED8C8C;
    margin-right: 20px;
}

.home {
    background: #95E7EE;
}

label , h1 {
    color: white;
}

/* .mianbg {
    color: #454545;
    border-radius: 50px;
} */


</style>