import { defineCollection, z } from 'astro:content';

const posts = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.date(),
    category: z.string(),
    tags: z.array(z.string()).default([]),
    podcast: z.string().optional(),
    guests: z.string().optional(),
    duration: z.string().optional(),
  }),
});

export const collections = { posts };
