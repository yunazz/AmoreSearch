export default {
  apps: [
    {
      name: "nuxt-app",
      script: ".output/server/index.mjs",
      interpreter: "node",
      exec_mode: "cluster",
      instances: "max",
      env: {
        NODE_ENV: "production",
        PORT: 3000,
      },
    },
  ],
};
