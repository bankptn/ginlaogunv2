<template>
    <v-container fluid class="main" id="Signup">
        <v-row justify="center" align="center">
            <v-form
                class="cardTitle"
                height="140px"
                width="350px"
            >
                <v-img
                    src="../assets/Group 9.svg"
                    contain
                    height="100px"
                    width="300px"
                />
                
            </v-form>
        </v-row>
        <v-row justify="center" align="center">
            <v-form
                class="cardBody"
                ref="form"
                v-model="valid"
                @submit.prevent="submitRegister"
                lazy-validation
            >  
            <div class="mainbg">
                <v-row>
                    <v-col cols="6">
                        <h1>SIGN UP</h1>
                    </v-col>
                    <v-col class="logoTitle" cols="6">
                        <v-card @click="onClickProfile" style="border-radius: 360px; min-width: 58px; min-height: 58px;">
                        <div class="profilepic">
                            <v-img 
                                src="../assets/user 1.svg"
                                height="150px"
                                width="150px"
                                contain
                            />
                            
                        </div>
                        </v-card>
                    </v-col>
                    <br>
                    <v-col cols="12">
                    <div class="add">
                        <h4>Add Profile Picture</h4>
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
                            :counter="15"
                            :rules="nameRules"
                            solo
                            name="fname"
                            required
                        />
                    </v-col>
                    <v-col cols="3">
                        <label>Last Name</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Last Name"
                            v-model=account.lname
                            :counter="15"
                            :rules="FnameRules"
                            required
                            solo
                            name="lname"
                        />
                    </v-col>
                    <v-col cols="6">
                        <label>ID Card Number</label>
                        <v-text-field
                            label="Regular"
                            placeholder="ID Card Number"
                            v-model=account.ssn
                            :rules="[rules.required, rulesssn.ssn]"
                            :counter="13"
                            solo
                            name="ssn"
                        />
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4">
                        <label>Date of Birth</label>
                        <!-- <v-text-field
                            label="Regular"
                            placeholder="Date of Birth"
                            v-model=account.birthDay
                            solo
                            name="birthDay"
                        /> -->
                        <v-menu
                            ref="menu1"
                            v-model="menu1"
                            :close-on-content-click="false"
                            transition="scale-transition"
                            offset-y
                            max-width="290px"
                            min-width="290px"
                            >
                            <template v-slot:activator="{ on, attrs }">
                                <v-text-field
                                
                                    label="Regular"
                                    placeholder="Date of Birth"
                                    v-model="dateFormatted"
                                    solo
                                    name="birthDay"

                                    hint="MM/DD/YYYY format"
                                    persistent-hint
                                    v-bind="attrs"
                                    @blur="date = parseDate(dateFormatted)"
                                    v-on="on"
                                    readonly
                                ></v-text-field>
                            </template>
                            <v-date-picker v-model="date" no-title @input="menu1 = false"></v-date-picker>
                            </v-menu>
                        
                    </v-col>
                    <v-col cols="5">
                        <label>Address</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Address"
                            v-model=account.address
                            :counter="50"
                            :rules="addressRules"
                            required
                            solo
                            name="address"
                        />
                    </v-col>
                    <v-col cols="3">
                        <label>Tel.</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Tel."
                            v-model=account.phoneNumber
                            :rules="[rules.required, rulestel.tel]"
                            :counter="10"
                            solo
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
                            :rules="[rules.required, rules.email]"
                            :counter="30"
                            solo
                            name="email"
                        />
                    </v-col>
                    <v-col cols="3">
                        <label>Username</label>
                        <v-text-field
                            label="Regular"
                            placeholder="Username"
                            v-model=account.username
                            :counter="15"
                            :rules="usernameRules"
                            required
                            solo
                            name="username"
                        />
                    </v-col>
                    <v-col cols="3">
                        <label>Password</label>
                        <v-text-field
                            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                            :rulespass="[rulespass.required, rulespass.min]"
                            :type="show1 ? 'text' : 'password'"
                            hint="At least 8 characters"
                            counter
                            @click:append="show1 = !show1"
                            solo
                            label="Regular"
                            placeholder="Password"
                            v-model=account.password
                            name="password"
                        />
                    </v-col>
                    <v-col cols="3">
                        <label>Re-Enter Password</label>
                        <v-text-field
                            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                            :rulespass="[rulespass.required, rulespass.min]"
                            :type="show2 ? 'text' : 'password'"
                            hint="At least 8 characters"
                            counter
                            @click:append="show2 = !show2"
                            label="Regular"
                            v-on:blur="validate"
                            placeholder="Re-Enter Password"
                            solo
                            name="re-password"
                            v-model="repassword"
                        />
                    </v-col>
                </v-row>
                
                <v-row justify="end" align="center">
                    <v-btn style="background-color: red; border-radius: 20px;" type="submit"
                        :disabled="!valid"
                        class="mr-4"
                        >
                        
                        Sign Up
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
        data: vm => ({
            date: new Date().toISOString().substr(0, 10),
            dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
            menu1: false,
            menu2: false,
            repassword: '',
            name: '',
            nameRules: [
                v => !!v || 'First Name is required',
                v => (v && v.length <= 15) || 'Name must be less than 10 characters',
            ],
            Fname: '',
            FnameRules: [
                v => !!v || 'Last Name is required',
                v => (v && v.length <= 15) || 'Name must be less than 10 characters',
            ],
            address: '',
            addressRules: [
                v => !!v || 'Address is required',
                v => (v && v.length <= 50) || 'Name must be less than 50 characters',
            ],
            username: '',
            usernameRules: [
                v => !!v || 'Username is required',
                v => (v && v.length <= 15) || 'Name must be less than 15 characters',
            ],
            
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
            rules: {
            required: value => !!value || 'ID Card Number is required',
            counter: value => value.length <= 30 || 'Max 30 characters',
            email: value => {
                const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                return pattern.test(value) || 'Invalid e-mail.'
                },
                },
                rulestel: {
            required: value => !!value || 'Tel is required',
            counter: value => value.length <= 10 || 'Max 10 characters',
            tel: value => {
                const pattern = /^[0-9]{10}$/
                return pattern.test(value) || 'Invalid phone number.'
                },
                },
                rulesssn: {
            required: value => !!value || 'E-Mail is required',
            counter: value => value.length <= 13 || 'Max 13 characters',
            ssn: value => {
                const pattern = /^[0-9]{13}$/
                return pattern.test(value) || 'Invalid ID card number.'
                },
                },
                show1: false,
                show2: false,
                
                password: 'Password',
                rulespass: {
                required: value => !!value || 'Required.',
                min: v => v.length >= 8 || 'Min 8 characters',
                },
            valid: true,
            passSame: true,
        }),

        computed: {
        computedDateFormatted () {
            return this.formatDate(this.date)
        },
        },
        watch: {
        date () {
            this.dateFormatted = this.formatDate(this.date)
        },
        },
    name:"Signup",
    
    methods: {
        onClickProfile () {
            this.$router.push({name:"refeel"})
        },
        submitRegister () {
            var state = this.$refs.form.validate()
            if (state) {
                this.account.birthDay = this.dateFormatted
                this.$store.dispatch({ 
                    type: "register",
                    ssn : this.account.ssn,
                    fname : this.account.fname,
                    lname : this.account.lname,
                    username : this.account.username,
                    password : this.account.password,
                    address : this.account.address,
                    email : this.account.email,
                    phoneNumber : this.account.phoneNumber,
                    birthDay : this.account.birthDay,
                })
            }
        },
        validate: function() {
            if (this.account.password !== this.repassword) {
                this.$store.dispatch({ type: 'dialog', state: true, msg: "Your Password doesn't match!" })
                this.passSame = false
            } else {
              this.passSame = true
            }
        },
        formatDate (date) {
            if (!date) return null

            const [year, month, day] = date.split('-')
            return `${month}/${day}/${year}`
        },
        parseDate (date) {
            if (!date) return null

            const [month, day, year] = date.split('/')
            return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
        },
        },
}


</script>

<style scoped>
.main{
    min-height: 100vh;
    background: url(../assets/home.svg) ;
    background-position: center;
    background-repeat: no-repeat;
    background-size: 145%;
}
.cardTitle{
    margin-top: 60px;
    margin-bottom: 20px;
    background-color: #454545;
    border-radius: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
}
/* .profilepic {
    background-color: white;
    border-radius: 360px;
    min-width: 58px;
    min-height: 58px;
    align-content: center;
    justify-items: center;
} */
.cardBody{
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
    /* background-color: red; */
}
.add {
    display: flex;
    justify-content: flex-end;
}
/* .mainbg {
    background: #454545;
    border-radius: 50px;
} */
label, h1, h4 {
    color: white;
}
</style>