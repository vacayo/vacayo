<template>
  <transition name="modal">
    <div class="modal fade modal-fill-in show" ref="modal" style="display: inherit !important;">
      <div class="modal-dialog" role="document">
        <div class="modal-content">

          <div class="modal-header">
            <slot name="header">
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
            </slot>
          </div>

        </div>
      </div>
    </div>
  </transition>
</template>

<script type="text/babel">
  export default {
    name: 'Modal',
    props: {
      name: String
    },
    mounted() {
      $(".modal[name='" + this.name + "']").modal()
    }
  }
</script>

<style>
  .modal-body {
    overflow-y: scroll !important;
  }

</style>