<template>
  <transition name="modal">
    <div class="modal fade" ref="modal" :name="name" tabindex="-1" role="dialog">
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
    data() {
      return {

      }
    },
    props: {
      name: String
    },
    methods: {
      show() {
        $(this.$refs.modal).modal('show');
      },
      hide() {
        $(this.$refs.modal).modal('hide');
      }
    },
    mounted() {
      this.hide()
    }
  }
</script>

<style>
  .modal-content {
    height: auto;
    min-height: 100%;
    border-radius: 0;
  }

  .modal-header {
    padding: 20px 30px;
  }

  .modal-body {
    padding: 20px 30px;
  }

  .modal-footer {
    padding: 20px 30px;
  }

  @media (min-width: 480px) {
    .modal-dialog {
      max-width: 720px;
      margin: 30px auto;
    }
  }

  @media (max-width: 575px) {
    .modal.fullscreen .modal-dialog {
      width: 100% !important;
      max-width: 100% !important;
      height: 100% !important;
      max-height: 100% !important;
      overflow: auto !important;
      margin: 0 !important;
      padding: 0 !important;
    }
  }

</style>