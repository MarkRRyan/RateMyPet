import React, {useContext} from 'react'
import AuthContext from '../context/AuthContext'

const LoginPage = () => {
    let { loginUser } = useContext(AuthContext)

    return(
        <div>
            <form on onSubmit={loginUser}>
                <input type='text' name='username' placeholder='Enter Username' />
                <input type='password' name='password' placeholder='EnterPassword' />
                <input type='submit' />
            </form>
        </div>
    )
}

export default LoginPage