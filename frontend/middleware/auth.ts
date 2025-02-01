export default defineNuxtRouteMiddleware(() => {
  if (!useCookie("auth_token").value) {
    return navigateTo("/login");
  }
});
