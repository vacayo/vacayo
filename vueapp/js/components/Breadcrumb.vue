<template>
  <ol class="breadcrumb breadcrumb-arrow">
    <li class="breadcrumb-item" v-for="(item, index) in list" v-bind:class="{ active:isLast(index) }">
      <span v-if="isLast(index)">{{ showName(item) }}</span>
      <router-link :to="item.path" v-else>{{ showName(item) }}</router-link>
    </li>
  </ol>
</template>

<script type="text/babel">
  export default {
    props: {
      list: {
        type: Array,
        required: true,
        default: () => []
      }
    },
    methods: {
      isLast (index) {
        return index === this.list.length - 1
      },
      showName (item) {
        if (item.meta && item.meta.label) {
          item = item.meta && item.meta.label
        }
        if (item.name) {
          item = item.name
        }
        return item
      }
    }
  }
</script>
