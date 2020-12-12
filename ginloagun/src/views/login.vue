<template>
  <v-container fluid class="main" id="login">
        <v-row justify="center" align="center">
            <v-form
                class="cardTitle"
            >
            <div class="titlebg">
                <v-img
                    src="../assets/Group 9.svg"
                    contain
                    height="100px"
                    width="300px"
                />
            </div>
            </v-form>
        </v-row>
        <v-row justify="center" align="center">
            <v-form
                class="cardBody"
                ref="form"
                v-model="valid"
                @submit.prevent="submitLogin"
                lazy-validation
            >  
                <div class="bg">
                    <v-row>
                        <v-col cols="10">
                            <h1>SIGN IN</h1>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="11">
                            <label>Username</label>
                            <v-text-field
                                label="Regular"
                                placeholder="Username"
                                v-model=account.username
                                solo
                            />
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="11">
                            <label>Password</label>
                            <v-text-field
                                label="Regular"
                                placeholder="Password"
                                v-model=account.password
                                solo
                                type="password"
                            />
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col cols="4">
                            <h3>New User?</h3>
                        </v-col>
                        <v-col cols="4" class="create">
                            <!-- <v-btn> -->
                                <h3><a href="/signup">create account</a></h3>
                                <!-- <h3>create account</h3> -->
                            <!-- </v-btn> -->
                            <!-- <v-card @click="onClickCreate" v-for="create in creates" :key="create.id" class="col">
                                {{ create.name }}
                            </v-card> -->
                        </v-col>
                        <v-col cols="4" justify="end" align="center" class="forgot">
                            <h3><a href="#">Forgot Password?</a></h3>
                        </v-col>

                    </v-row>
                    <v-row justify="end" align="center">
                        <v-btn style="background-color: red; border-radius: 20px;" type="submit" >
                            Sign In
                        </v-btn>
                    </v-row>
                </div>
            </v-form>
        </v-row>
        <!-- Dialog -->
        <v-dialog
            v-model="$store.getters.getDialogState"
            width="500"
            persistent
        >
            <v-card>
                <v-card-title class="headline grey lighten-2">ALERT</v-card-title>
                    <v-card-text> {{ $store.getters.getDialogMessage }} </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                            <v-btn color="primary" @click="$store.dispatch({ type: 'dialog', state: false, msg:'' })">
                                ok
                            </v-btn>
                    </v-card-actions>
            </v-card>
        </v-dialog>
        <!-- Loading -->
        <v-overlay :value="$store.getters.getLoadingDialog">
            <v-progress-circular indeterminate size="64"/>
        </v-overlay>
    </v-container>
</template>

<script>
export default {
name: "login",
    data() {
        return {
            valid: true,
            creates:[
                {
                    id:"1",
                    name:"create an account",
                }
            ],
            account:{
                username: "",
                password: ""
            }
        }
    },
    methods: {
        onClickCreate () {
            this.$router.push({name:"Signup"})
        },
        submitLogin () {
            this.$store.dispatch({ 
                type: "login",
                username : this.account.username,
                password : this.account.password,
            })
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
.titlebg {
    background: #454545;
    border-radius: 50px;
    
}
.cardTitle{
    margin-top: 80px;
    margin-bottom: 20px;
    background-color: #454545;
    border-radius: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.cardBody {
    margin-top: 10px;
    background-color: #454545;
    border-radius: 30px;
    padding: 20px;
    /* height: 100%;
    width: 60%; */
    /* justify-content: ; */
    justify-content: center;
    align-items: center;
    min-width: 700px;
    min-height: 450px;
}
.bg {
    background-color: #454545;
    justify-content: center;
    align-items: center;
    margin-left: 30px;
}
label, h3, h1 {
    color: white;
}
.create a{
    text-decoration: none;
    color: #8DEF84;
}

.forgot a{
    text-decoration: none;
    color: cyan;
}
</style>