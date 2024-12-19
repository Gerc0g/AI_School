import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Функция для отправки сообщений чата
export const sendMessage = async (message) => {
  try {
    const response = await api.post('/chat', { msg: message });
    return response.data;
  } catch (error) {
    throw error;
  }
};
