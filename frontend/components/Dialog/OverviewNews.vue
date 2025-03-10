<script setup>
const props = defineProps({
  is_active: { type: Boolean, required: true },
  item: {
    type: Object,
  },
});

const emit = defineEmits(["update:is_active", "close"]);

const form = ref({});

function onDialogChange(val) {
  emit("update:is_active", val);
}
</script>

<template>
  <ClientOnly>
    <v-dialog
      :model-value="is_active"
      scrollable
      width="800"
      @update:model-value="onDialogChange"
      persistent
    >
      <v-card>
        <button
          class="icon--dialog-close"
          variant="text"
          @click="onDialogChange(false)"
        >
          <v-icon icon="mdi-close" size="large" />
        </button>
      </v-card>
    </v-dialog>
  </ClientOnly>
</template>
