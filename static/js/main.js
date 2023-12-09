$(() => {

     $('#signup').on('click', () => {
        $('body').append($('<div/>', {
          id: 'overlay'
        }));
        $('#overlay').append('<div class="popup" id="signin-popup">\
        <a href="#" class="close">X</a>\
        <form method="post">\
           <h2>Sign up</h2>\
           <form method="post">\
           <input type="text" name="name" placeholder="Name">\
            <input type="email" name="email" placeholder="E-mail">\
            <input type="password" name="password" placeholder="Password">\
            <input type="password" name="confirm-password" placeholder="Confirm password">\
            <input type="submit" value="Sign up">\
           </form>\
           <span>Dont have an account?&nbsp;&nbsp;<a href="">Register here</a></span>\
      </div>')

      $('.close').on('click', () => {
        $('#overlay').remove()
       })

     })
     $('#login').on('click', () => {
        $('body').append($('<div/>', {
          id: 'overlay'
        }));
        $('#overlay').append('<div class="popup" id="login-popup">\
        <a href="#" class="close">X</a>\
          <form method="post">\
             <h2>Log in</h2>\
             <form method="post">\
              <input type="email" name="email" placeholder="E-mail">\
              <input type="password" name="password" placeholder="Password">\
              <input type="submit" value="Login in">\
             </form>\
             <span>Dont have an account?&nbsp;&nbsp;<a href="">Register here</a></span>\
        </div>')

        $('.close').on('click', () => {
            $('#overlay').remove()
        })
     })
});