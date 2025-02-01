export async function apiFetch(endpoint: string, options: RequestInit = {}) {
  const token = useCookie("auth_token").value;

  const headers = {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Token ${token}` } : {}),
  };

  const response = await fetch(`http://localhost:8000${endpoint}`, {
    ...options,
    headers,
  });

  return response.json();
}
