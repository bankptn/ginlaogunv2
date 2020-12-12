<template>
  <v-container fluid class="main" id="reserve">
      <v-row justify="center" align="center">
        <v-form
            class="cardBody"
        >
            <div class="mainbg">
                <v-row>
                    <v-col cols="8" class="map">
                        <v-img src="../assets/Refeel ผังร้าน 2.svg" alt="refeel" contain />
                    </v-col>
                    <v-col cols="4">
                        <h1>Book Table</h1>
                        <br>
                        <v-row>
                            <h2>First Name:</h2>
                            <v-text-field
                                label="Regular"
                                placeholder="First Name"
                                solo
                            />
                        </v-row>
                        <v-row>
                            <h2>Last Name:</h2>
                            <v-text-field
                                label="Regular"
                                placeholder="Last Name"
                                solo
                            />
                        </v-row>
                        <v-row>
                            <h2>E-Mail:</h2>
                            <v-text-field
                                label="Regular"
                                placeholder="E-Mail"
                                solo
                            />
                        </v-row>
                        <v-row>
                            <h2>Tel:</h2>
                            <v-text-field
                                label="Regular"
                                placeholder="Tel."
                                solo
                            />
                        </v-row>
                        <v-row>
                            <h2>Date:</h2>
                            <v-text-field
                                label="Regular"
                                placeholder="Date"
                                solo
                            />
                        </v-row>
                        <v-row>
                            <h2>Time:</h2>
                            <v-text-field
                                label="Regular"
                                placeholder="Time"
                                solo
                            />
                        </v-row>
                        <v-row class="btn">
                            <v-btn class="submit" style="background-color: #95E7EE; border-radius: 20px;" @click="onClickSubmit">
                                Submit
                            </v-btn>
                            <v-btn class="cancel" style="background-color: #ED8C8C; border-radius: 20px;">
                                Cancel
                            </v-btn>
                        </v-row>
                        
                    </v-col>
                </v-row>
            </div>
        </v-form>
      </v-row>

  </v-container>
</template>

<script>
export default {
    name:"reserve",
    methods: {
        onClickSubmit() {
            console.log(),
            this.$router.push({name:"refeel"})
        }
    }

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
    margin-top: 78px;
    height: 70vh;
    width: 70vw;
    background: #454545;
    border-radius: 50px;
}
.mainbg {
    padding: 45px;
    background-color: #454545;
    border-radius: 50px;
}
h1, h2 {
    /* margin-left: 40px; */
    color: white;
}
.btn {
    display: flex;
    justify-content: flex-end;
}
.submit {
    margin-right: 20px;
}
h2 {
    margin-right: 2 px;
}
.cardBody {
    margin-top: 20px;
}
</style>