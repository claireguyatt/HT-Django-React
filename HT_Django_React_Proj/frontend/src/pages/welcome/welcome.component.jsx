import { Link } from "react-router-dom";

import './welcome.styles.css';

const Welcome = () => {
    return (

        <div id='homepage-container'>
            <h1>What makes you happy?</h1>
            <Link to='/login'>Log In</Link>
            <Link to='/register'>Register</Link>
            <Link to="/explore">Explore site as a guest</Link>
        </div>

    );
};

export default Welcome;