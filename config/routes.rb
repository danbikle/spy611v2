Rails.application.routes.draw do
  get  'posts/index'
  root 'posts#index'
  get ':controller(/:action)'
  get 'contact'   => 'posts#contact'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
