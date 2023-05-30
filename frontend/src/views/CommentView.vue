<template>
  <div class="mt-3">
    <h3>Comments Section</h3>
    <div class="d-flex justify-content-center pt-3 pb-2"><input v-on:keyup.enter="sendComment" v-model="comment_text"
                                                                type="text" name="text"
                                                                placeholder="Ask Questions"
                                                                class="form-control addtxt">
    </div>
    <div v-for="comment in comments" :key="comment.id">
      <div class="d-flex justify-content-center py-2">
        <div class="second py-2 px-2"><span class="text1">{{ comment.text }}</span>
          <div class="d-flex justify-content-between py-1 pt-2">
            <div><img :src="comment.user.image" width="18"><span
                class="text2">{{ comment.user.username }}</span></div>
            <!--            <div><span class="text3">Upvote?</span><span class="thumbup"><i class="fa fa-thumbs-o-up"></i></span><span-->
            <!--                class="text4">3</span></div>-->
          </div>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "CommentView",
  data() {
    return {
      comment_text: null,
      comments: [],
      user: {}
    }
  },
  methods: {
    getUser() {
      axios
          .get("http://127.0.0.1:8000/logged_in_user/")
          .then((response) => {
            // console.log(response.data)
            this.user = response.data
          })
          .catch((error) => {
            console.log(error);
          });
    },
    sendComment() {
      console.log(this.comment_text)
      axios
          .post("http://127.0.0.1:8000/api/comments/", {
            author: this.user.id,
            text: this.comment_text,
            item: this.$router.history.current.params.id,
          })
          .then((response) => {
            console.log(response.data)
            this.comment_text = null
            this.getComments()
          })
          .catch((error) => {
            console.log(error);
          });
    },
    getComments() {
      axios
          .get("http://127.0.0.1:8000/api/comments/item/" + this.$router.history.current.params.id)
          .then((response) => {
            // console.log(response.data)
            this.comments = response.data
          })
          .catch((error) => {
            console.log(error);
          });
    },
  },
  mounted() {
    this.getComments()
    this.getUser()
  }
}
</script>

<style>


.addtxt {
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
  font-size: 13px;
  width: 350px;
  background-color: #e5e8ed;
  font-weight: 500;
}

.form-control: focus {
  color: #000;
}

.second {
  width: 350px;
  background-color: white;
  border-radius: 4px;
  box-shadow: 10px 10px 5px #aaaaaa;
}

.text1 {
  font-size: 13px;
  font-weight: 500;
  color: #56575b;
}

.text2 {
  font-size: 13px;
  font-weight: 500;
  margin-left: 6px;
  color: #56575b;
}

.text3 {
  font-size: 13px;
  font-weight: 500;
  margin-right: 4px;
  color: #828386;
}

.text3o {
  color: #00a5f4;

}

.text4 {
  font-size: 13px;
  font-weight: 500;
  color: #828386;
}

.text4i {
  color: #00a5f4;
}

.text4o {
  color: white;
}

.thumbup {
  font-size: 13px;
  font-weight: 500;
  margin-right: 5px;
}

.thumbupo {
  color: #17a2b8;
}
</style>