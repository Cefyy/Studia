import { useState } from 'react'
import type { FormEvent } from 'react'

import { useRecipeStore } from '../useRecipeStore'

import './AddRecipeForm.css'

export default function AddRecipeForm() {
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const addRecipe = useRecipeStore((state) => state.addRecipe)

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    if (!title.trim() || !content.trim()) {
      return
    }

    addRecipe({ title, content })
    setTitle('')
    setContent('')
  }

  return (
    <form className="add-recipe-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Recipe Title"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
      />
      <textarea
        placeholder="Recipe Content"
        value={content}
        onChange={(event) => setContent(event.target.value)}
      />
      <button type="submit">Add Recipe</button>
    </form>
  )
}