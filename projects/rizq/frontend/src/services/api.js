// API Service - Connects frontend to backend
const API_URL = import.meta.env.VITE_API_URL || "http://localhost:3001";

async function handleResponse(response) {
  if (!response.ok) {
    const error = await response
      .json()
      .catch(() => ({ error: "Request failed" }));
    throw new Error(error.error || `HTTP ${response.status}`);
  }
  return response.json();
}

export const api = {
  async health() {
    const response = await fetch(`${API_URL}/api/health`);
    return handleResponse(response);
  },

  async getJobs(filters = {}) {
    const params = new URLSearchParams();

    if (filters.location) params.append("location", filters.location);
    if (filters.remote !== undefined) params.append("remote", filters.remote);
    if (filters.type) params.append("type", filters.type);
    if (filters.halal !== undefined) params.append("halal", filters.halal);
    if (filters.limit) params.append("limit", filters.limit);
    if (filters.offset) params.append("offset", filters.offset);

    const queryString = params.toString();
    const url = `${API_URL}/api/jobs${queryString ? `?${queryString}` : ""}`;

    const response = await fetch(url);
    return handleResponse(response);
  },

  async getJob(id) {
    const response = await fetch(`${API_URL}/api/jobs/${id}`);
    return handleResponse(response);
  },

  async searchJobs(query, limit = 20, offset = 0) {
    const params = new URLSearchParams({
      q: query,
      limit: limit.toString(),
      offset: offset.toString(),
    });

    const response = await fetch(`${API_URL}/api/jobs/search?${params}`);
    return handleResponse(response);
  },

  async getStats() {
    const response = await fetch(`${API_URL}/api/stats`);
    return handleResponse(response);
  },
};

export default api;
