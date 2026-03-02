import { ChatOpenAI } from "@langchain/openai";
import { ChatGroq } from "@langchain/groq";

// If you have a direct OpenAI API Key
// export const llm = new ChatOpenAI({
//     openAIApiKey: process.env.OPENAI_API_KEY,
//     modelName: "gpt-4.1" // or whatever model you use
// });

// Since the Python code used LiteLLM pointing to a custom proxy,
// we use ChatOpenAI in TypeScript but override the baseUrl to point to LiteLLM.
// LiteLLM is fully compatible with the OpenAI API format!
// export const llm = new ChatOpenAI({
//   apiKey: process.env.LITELLM_API_KEY || "dummy",
//   modelName: "litellm_proxy/gpt-5",
//   configuration: {
//     baseURL: "https://llm.keyvalue.systems", // Assuming this is your LiteLLM proxy URL
//   },
// });


export const llm = new ChatGroq({
  apiKey: process.env.GROQ_API_KEY,
  model: "openai/gpt-oss-120b",
  temperature: 0,
});