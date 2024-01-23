<template>
  <div class="card">
    <div class="card-header">Enter your login credentials:</div>
    <div class="card-body">
      <form name="login-form">
        <div class="mb-3 row">
          <label for="inputUsername" class="col-sm-2 col-form-label">Username:</label>
          <div class="col-sm-10">
            <input type="text" class="form-control" id="inputUsername"
                   value="email@example.com"
                   v-model="input.username">
          </div>
        </div>
        <div class="mb-3 row">
          <label for="inputPassword" class="col-sm-2 col-form-label">Password:</label>
          <div class="col-sm-10">
            <input type="password" class="form-control" id="inputPassword"
                  v-model="input.password">
          </div>
        </div>
        <button class="btn btn-outline-primary float-end"
                type="submit" @click.prevent="login()">
          Login
        </button>
      </form>
  </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const input = ref({
  username: '',
  password: ''
})

function login() {
  //make sure username OR password are not empty
  console.log(`username: ${input.value.username}`)
  console.log(`password: ${input.value.password}`)
  if(input.value.username != "" && input.value.password != ""){
    console.log("authenticated")
  }else{
    console.log("Username and Password can not be empty")
  }
}

onMounted(() => {
  console.log('Component mounted!!!')
  input.value = {
    username: '',
    password: '',
  }
});

</script>

<style scoped>

</style>