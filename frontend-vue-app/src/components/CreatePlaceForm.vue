<template>
  <div class="container">
    <h1>Create New Place</h1>
  <div class="card">
    <div class="card-header">Create place</div>
    <div class="card-body">
      <form @submit.prevent="handleSubmit" ref="placeForm">
        <div class="mb-3">
          <label for="name">Name:</label>
          <input v-model="formData.name"
                 type="text"
                 id="name"
                 name="name"
                 placeholder="Name"
                 class="form-control"
                 required />
        </div>

        <div class="mb-3">
          <label for="description">Description:</label>
          <textarea v-model="formData.description"
                    id="description"
                    name="description"
                    class="form-control"
                    placeholder="Description..." required />
        </div>
        <div class="mb-3 form-check">
          <input v-model="formData.coffee"
                   type="checkbox"
                   id="coffee"
                   class="form-check-input"
                   name="coffee" />
          <label for="coffee" class="form-check-label">Has Coffee:</label>
        </div>

        <div class="mb-3 form-check">
          <input v-model="formData.food" type="checkbox" id="food"
                 class="form-check-input"
                 name="food" />
          <label for="food" class="form-check-label">Has Food:</label>
        </div>

        <div class="mb-3 form-check">
          <input v-model="formData.wifi" type="checkbox" id="wifi"
                 class="form-check-input"
               name="wifi" />

          <label for="wifi" class="form-check-label">Has Wifi:</label>
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text" id="latitude">Latitude:</span>
          <input v-model.number="formData.lat"
                 type="number"
                 class="form-control"
                 id="latitude"
                 name="latitude"
                 placeholder="Latitude..."
                 aria-label="Latitude"
                 aria-describedby="latitude"
          />
        </div>

         <div class="input-group mb-3">
          <span class="input-group-text" id="longtitude">Longtitude:</span>
          <input v-model.number="formData.lng"
                 type="number"
                 class="form-control"
                 id="longtitude"
                 name="longtitude"
                 placeholder="Longtitude..."
                 aria-label="Longtitude"
                 aria-describedby="longtitude"
          />
        </div>

        <button type="submit" class="btn btn-primary">Submit</button>

      </form>

  </div>
  </div>
  </div>
</template>

<script setup>
  import { ref, defineEmits, defineProps } from 'vue'

  defineProps({
    msg: String
  })

  const emit = defineEmits(["submit"])

  let formData = ref({
    name: "",
    description: "",
    coffee: false,
    food: false,
    wifi: false,
    lat: 0,
    lng: 0
  })

  const handleSubmit = () => {
    console.log('handleSubmit() called')
    emit("submit", formData);
  }

  // eslint-disable-next-line no-unused-vars
  const resetForm = () => {
    console.log('resetForm() called')
    formData.value = {
      name: "",
      description: "",
      coffee: false,
      food: false,
      wifi: false,
      lat: 0,
      lng: 0,
    }
  }

  // eslint-disable-next-line no-undef
  defineExpose({
    resetForm
  })
</script>

<style scoped>
/* Add your component styles here */
</style>