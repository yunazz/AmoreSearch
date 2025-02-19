module.exports = {
  apps: [
    {
      name: "nuxt-app",
      script: ".output/server/index.mjs", // Nuxt3 빌드된 서버 파일 경로
      exec_mode: "cluster",
      instances: "max",
      env: {
        NODE_ENV: "production",
        PORT: 3000,
      },
    },
  ],
};
