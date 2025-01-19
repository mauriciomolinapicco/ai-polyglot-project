import { useState } from 'react'

const Box = ({translate}) => {
    const [text, setText] = useState('') 
    const [selectedOption, setSelectedOption] = useState('')

    const handleSelectChange = (e) => {
        setSelectedOption(e.target.value);
    }

    const onSubmit = (e) => {
        e.preventDefault()
        if (!text) {
            alert('You have to add a text to translate')
            return
        }
        translate({text, selectedOption: selectedOption || 'French'})
    }

    return (
    <div>
        
      <form onSubmit={onSubmit}>
        <label>Text to translate 👇</label>
        <textarea id='text-input' rows="3" value={text} 
            onChange={(e) => setText(e.target.value) } ></textarea>
        <label>Select language 👇</label>
        <select id='options' value={selectedOption} onChange={handleSelectChange}>
            <option value="French" >French</option>
            <option value="Portuguese" >Portuguese</option>
            <option value="Japanese" >Japanese</option>
        </select>
        <input type="submit" value="Translate"/>
      </form>
    </div>
  )
}

export default Box