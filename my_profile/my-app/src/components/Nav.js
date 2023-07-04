import './Nav.css';








function Nav() {
    return(

        <>
        <div  className='nav-item my-3 w-28 '>
            <nav className="flex justify-center space-x-4">
                <a href="/dashboard" className="font-medium px-3 py-2 text-purple-700  hover:text-white rounded-full border  hover:bg-purple-500  hover:border-transparent focus:outline-none focus:ring-2 focus:ring-purple-600 focus:ring-offset-2">Home</a>
                <a href="/team" className="font-medium px-3 py-2 text-purple-700  hover:text-white rounded-full border  hover:bg-purple-500  hover:border-transparent focus:outline-none focus:ring-2 focus:ring-purple-600 focus:ring-offset-2">Team</a>
                <a href="/projects" className="font-medium px-3 py-2 text-purple-700  hover:text-white rounded-full border  hover:bg-purple-500  hover:border-transparent focus:outline-none focus:ring-2 focus:ring-purple-600 focus:ring-offset-2">Projects</a>
                <a href="/reports" className="font-medium px-3 py-2 text-purple-700  hover:text-white rounded-full border  hover:bg-purple-500  hover:border-transparent focus:outline-none focus:ring-2 focus:ring-purple-600 focus:ring-offset-2">Reports</a>
            </nav>

            
        </div>


        
        </>
    );
}

export default Nav;