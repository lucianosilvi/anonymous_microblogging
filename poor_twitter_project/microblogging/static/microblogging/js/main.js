const API_URL = "http://localhost:8000"

new Vue({
  el: '#app',
  delimiters: ['%{', '}'],  // Delimiters redefined for Django templates
  data: {
      message: '',
      name: '',
      tweets: [],
      result_message: ''
  },
  computed: {
  },
  components: {
  },
  methods: {
    get_tweets: function () {
      let url = `${API_URL}/tweets/`
      axios.get(url)
        .then(response => {
          console.log(response)
          if (response.data.length > 0)
            this.tweets = response.data
        })
        .catch(function (error) {
          console.log(error)
          alert(error)
        })
    },
    save: function () {
      axios.post(`${API_URL}/save`,
        {
          name: this.name,
          message: this.message
        })
        .then(response => {
          console.log(response)
          this.result_message = response.data.msg
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  created () {
    setInterval(() => {
        this.get_tweets()
    }, 1000);
  }
})
