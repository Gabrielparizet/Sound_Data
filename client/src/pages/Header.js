export default function Header (){


    return (
        <>
            <header class="text-gray-500 font-mono">
                <div>
                    <nav>
                        <div className="flex justify-center text-gray-500 text-4xl font-semibold">
                            <h1 className="font-bold uppercase p-4 border-b border-gray-100">
                                <a href="/" class="text-red-500">Sound Data</a>
                            </h1>
                        </div>
                        <ul className="pl-6">
                            <li className="justify-between text-gray-700 font-bold" >
                                <a href="#">
                                    <span>Home</span>
                                </a>
                            </li>
    
                            <li className="text-gray-700 font-bold">
                                <a href="#">
                                    <span>About</span>
                                </a>
                            </li>
                            <li className="text-gray-700 font-bold">
                                <a href="#">
                                    <span>Contact</span>
                                </a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </header>
        </>
    );

};