<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

  <div id="bottomMid"> 
        
    <div class="cardOne">
        <div class="imageHolder">
            <img class="card-img-top" src="{{ club.main_picture }}" alt="Card image cap">
        </div>
        <div class="card-body">
            <h5 class="card-title">{{ club.name }}</h5>
            <p class="card-text">{{ club.description }}</p>
            <a class="btn btn-primary">Learn More</a>
        </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      posts: [],
      errors: []
    }
  },

  // Fetches posts when the component is created.
  async created() {
    try {
      const response = await axios.get(`http://localhost:8000/club/`, {
        headers: {
          Accept: 'application/json'
        }
      })
      this.club = response.data
    } catch (e) {
      this.errors.push(e)
    }
  }
}
</script>

<style scoped>
#topMid{
    height:25%;
    display:flex;
    justify-content:center;
    align-items: center;
}

#mid{
    width:100%;
    display:flex;
}
</style>
