import { ref } from 'vue'
import axios from "axios";

export default function () {
    const apiPlaces = ref([])
    const apiPlaceCreated = ref(false)

    const apiPlaceDetail = ref(null)
    const apiPlaceDetailFetched = ref(false)

    const apiEditPlaceFormData = ref(null)
    const apiEditPlaceEnabled = ref(false)

    const apiPlaceUpdated = ref(false)

    async function apiGetPlaceList() {
        console.log('----------------------------------');
        console.log('apiGetPlaceList() called')
        console.log('----------------------------------');
        axios.get("http://localhost:5000/places")
            .then((response) => {
                console.log('data is returned')
                console.log(response.data)
                apiPlaces.value = response.data
            })
            .catch(error => {
                console.error('Error querying places', error)
            })
    }

    async function apiAddPlace(placeData){
      apiPlaceCreated.value = false;
      axios.post("http://localhost:5000/places", placeData.value).then((response) => {
         console.log("Data submitted successfully", response.data);

         apiPlaceCreated.value = true

      })
      .catch((error) => {
        console.error("Error submitting data", error);
      });
    }

    async function apiGetPlaceDetail(place_id) {
        apiPlaceDetailFetched.value = false;
        axios.get(`http://localhost:5000/place/${place_id}`)
            .then((response) => {
                console.log('we have detail data!')
                console.log(response.data)
                apiPlaceDetail.value = response.data;
                apiPlaceDetailFetched.value = true;
            })
            .catch(error => {
                console.error('Error querying place details!', error)
            })
    }

    async function apiDeletePlace(place_id) {
        axios.delete(`http://localhost:5000/place/${place_id}`)
            .then((response) => {
                console.log(response.data)
                if (response.data.success) {
                    apiGetPlaceList()
                } else {
                    // console.error(response.data.error)
                    console.error('Some error occurred while deleting!')
                }
            })
            .catch(error => {
                console.error('Error deleting place!', error)
            })
    }

    async function apiEditPlace(place_id) {
      console.log(`apiEditPlace(${place_id})`);
      apiEditPlaceEnabled.value = false
      axios.get(`http://localhost:5000/place/${place_id}`)
        .then((response) => {
          console.log(response.data)
          apiEditPlaceFormData.value = response.data
          apiEditPlaceEnabled.value = true
        })
        .catch(error => {
          console.error('Error deleting place!' , error)
        })
    }

    async function apiUpdatePlace(placeData){
      console.log('updatePlace() called')
      apiPlaceUpdated.value = false
      axios.put(`http://localhost:5000/places/${placeData.value.id}`, placeData.value)
          .then((response) => {
             console.log("Data updated successfully", response.data);
             apiPlaceUpdated.value = true
        })
        .catch((error) => {
            console.error("Error submitting data", error);
        });
    }

    return {
        apiPlaces,
        apiGetPlaceList,

        apiAddPlace,
        apiPlaceCreated,

        apiGetPlaceDetail,
        apiPlaceDetail,
        apiPlaceDetailFetched,

        apiDeletePlace,

        apiEditPlace,
        apiEditPlaceEnabled,
        apiEditPlaceFormData,

        apiUpdatePlace,
        apiPlaceUpdated,

    }
}