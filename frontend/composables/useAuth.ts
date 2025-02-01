export function useAuth() {
  const authToken = useCookie("auth_token");

  async function login(username: string, password: string) {
    const response = await fetch(
      "http://localhost:8000/api/auth/token/login/",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      }
    );

    const data = await response.json();
    if (response.ok) {
      authToken.value = data.auth_token; // Save token in cookie
      return true;
    } else {
      throw new Error(data.non_field_errors?.[0] || "Login failed");
    }
  }

  async function logout() {
    await fetch("/api/auth/token/logout/", { method: "POST" });
    authToken.value = null; // Remove token
  }

  async function getUser() {
    return fetch("/api/auth/users/me/");
  }

  return { authToken, login, logout, getUser };
}
