<template>
  <el-row class="header" type="flex" justify="space-around">
    <el-col :xs="0" :sm="3"></el-col>
    <el-col :xs="12" :sm="9">
      <div class="logo">
        <img :src="logo" alt="Vacayo: Begin at Home" />
      </div>
    </el-col>
    <el-col :xs="12" :sm="9">
      <div class="quote">
        <div>Quote Range</div>
        <div>{{ quote }}</div>
      </div>
    </el-col>
    <el-col :xs="0" :sm="3"></el-col>
  </el-row>
</template>

<script type="text/babel">
import logo from '../../../assets/img/vacayo-logo-horiz-white_1.png'

export default {
  data() {
    return {
      logo: logo
    }
  },
  computed: {
    quote: {
      get () {return this.$store.state.quote},
      set (value) {this.$store.commit('setQuote', value)}
    }
  },

  methods: {
  }
}
</script>

<style>
.header {
  background-color: #424242;
  min-height: 76px;
  margin-bottom: 50px;
}

.logo img {
  height: 72px;
}

.quote div {
  margin: 20px;
  color: #EEEEEE;
  font-weight: bold;
  text-align: right;
}
</style>