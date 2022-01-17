

ns=$1
list=($( kubectl get pods -n $ns  | awk '{print $1}'))
for object in "${list[@]}" ; do

kubectl get pod $object  -n $ns -o jsonpath='{.spec.containers[].image}{"\n"}'
done

