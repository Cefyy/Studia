import { create } from 'zustand'

import type { Recipe } from './types'

interface AddRecipeInput {
  title: string
  content: string
}

interface RecipeStore {
  recipes: Recipe[]
  showOnlyFavorites: boolean
  searchTerm: string
  addRecipe: (recipe: AddRecipeInput) => void
  deleteRecipe: (id: number) => void
  toggleFavorite: (id: number) => void
  setShowOnlyFavorites: (value: boolean) => void
  setSearchTerm: (value: string) => void
}

const initialRecipes: Recipe[] = [
  {
    id: 1,
    title: 'Spaghetti Bolognese',
    content: 'Classic Italian dish with a rich tomato and beef sauce.',
    isFavorite: false,
  },
  {
    id: 2,
    title: 'Chicken Curry',
    content: 'Spicy and flavorful curry served best with rice.',
    isFavorite: true,
  },
]

const normalizeSearchTerm = (value: string) => value.trim().toLowerCase()

export const useRecipeStore = create<RecipeStore>((set) => ({
  recipes: initialRecipes,
  showOnlyFavorites: false,
  searchTerm: '',
  addRecipe: ({ title, content }) =>
    set((state) => {
      const trimmedTitle = title.trim()
      const trimmedContent = content.trim()

      if (!trimmedTitle || !trimmedContent) {
        return {}
      }

      const newRecipe: Recipe = {
        id: Date.now(),
        title: trimmedTitle,
        content: trimmedContent,
        isFavorite: false,
      }

      return { recipes: [...state.recipes, newRecipe] }
    }),
  deleteRecipe: (id) =>
    set((state) => ({
      recipes: state.recipes.filter((recipe) => recipe.id !== id),
    })),
  toggleFavorite: (id) =>
    set((state) => ({
      recipes: state.recipes.map((recipe) =>
        recipe.id === id ? { ...recipe, isFavorite: !recipe.isFavorite } : recipe,
      ),
    })),
  setShowOnlyFavorites: (value) => set({ showOnlyFavorites: value }),
  setSearchTerm: (value) => set({ searchTerm: value }),
}))

export const selectVisibleRecipes = (state: RecipeStore): Recipe[] => {
  let recipes = state.recipes

  if (state.showOnlyFavorites) {
    recipes = recipes.filter((recipe) => recipe.isFavorite)
  }

  const searchTerm = normalizeSearchTerm(state.searchTerm)

  if (searchTerm) {
    recipes = recipes.filter((recipe) => {
      const title = recipe.title.toLowerCase()
      const content = recipe.content.toLowerCase()

      return title.includes(searchTerm) || content.includes(searchTerm)
    })
  }

  return recipes
}