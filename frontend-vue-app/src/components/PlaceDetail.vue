<template>
  <div class="container">
    <h1>Place detail</h1>
    <div class="card">
      <div class="card-header">
        Place details #{{ data.id }}
         <button
              class="btn btn-danger float-end"
              @click="deletePlace(data.id)">Delete Place</button>
      </div>
      <div class="card-body">
        <table class="table table-responsive table-bordered">
          <thead>
            <th></th>
            <th></th>
          </thead>
          <tbody>
            <tr>
              <th>Name</th>
              <td>{{ data.name }}</td>
            </tr>
            <tr>
              <th>Description</th>
              <td>{{ data.description }}</td>
            </tr>
            <tr>
              <th>Has coffee?</th>
              <td>{{ data.coffee }}</td>
            </tr>
            <tr>
              <th>Has food?</th>
              <td>{{ data.food }}</td>
            </tr>
            <tr>
              <th>Has Wifi</th>
              <td>{{ data.wifi }}</td>
            </tr>
            <tr>
              <th>Latitude</th>
              <td>{{ data.lat }}</td>
            </tr>
            <tr>
              <th>Longtitude</th>
              <td>{{ data.lng }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

</template>

<script setup>
// eslint-disable-next-line no-unused-vars
import {ref, defineProps, defineEmits } from 'vue';

// eslint-disable-next-line no-unused-vars
const props = defineProps({
  data: Object, // ref(null)
})

const emit = defineEmits(["delete_place"])

const deletePlace = (id) => {
  console.log(`about to emit delete_place event with arg ${id}`)
  emit('delete_place', id)
}

</script>

<style scoped>

</style>